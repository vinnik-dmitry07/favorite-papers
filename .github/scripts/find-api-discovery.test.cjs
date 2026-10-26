'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const { findApiDiscovery } = require('./find-api-discovery.cjs');

const repository = { id: 10, full_name: 'owner/papers' };

function artifact(id, extra = {}) {
  return {
    id, name: 'agent-api-discovery', expired: false,
    workflow_run: {
      id, repository_id: 10, head_repository_id: 10,
      head_branch: 'main', head_sha: `sha-${id}`,
    },
    ...extra,
  };
}

function run(id, extra = {}) {
  return {
    id, workflow_id: 7, status: 'completed', conclusion: 'success',
    event: 'workflow_dispatch', head_branch: 'main', head_sha: `sha-${id}`,
    head_repository: repository, repository, ...extra,
  };
}

function fixture(pages, runs = {}) {
  const calls = [];
  const github = { rest: { actions: {
    async listArtifactsForRepo(args) {
      calls.push(['artifacts', args]);
      assert.equal(args.name, 'agent-api-discovery');
      assert.equal(args.per_page, 100);
      return { data: { artifacts: pages[args.page - 1] || [] } };
    },
    async getWorkflow(args) {
      calls.push(['workflow', args]);
      assert.equal(args.workflow_id, 'agent-api.yml');
      return { data: { id: 7 } };
    },
    async getWorkflowRun(args) {
      calls.push(['run', args]);
      return { data: runs[args.run_id] || run(args.run_id) };
    },
    async listWorkflowRuns() {
      throw new Error('Recent workflow runs must not limit discovery');
    },
  } } };
  return {
    calls,
    find: () => findApiDiscovery({ github, owner: 'owner', repo: 'papers' }),
  };
}

test('publication survives arbitrarily many newer successful probe runs', async () => {
  // Runs 2..1001 are successful probes without a discovery artifact.
  const mock = fixture([[artifact(1)]]);
  assert.deepEqual(await mock.find(), { runId: 1, artifactId: 1 });
  assert.deepEqual(mock.calls.map(([kind]) => kind), ['artifacts', 'workflow', 'run']);
});

test('paginates discovery artifacts and skips expired entries', async () => {
  const expired = Array.from({ length: 100 }, (_, i) => artifact(200 + i, { expired: true }));
  const mock = fixture([expired, [artifact(10)]]);
  assert.deepEqual(await mock.find(), { runId: 10, artifactId: 10 });
  assert.equal(mock.calls.filter(([kind]) => kind === 'artifacts').length, 2);
  assert.equal(mock.calls.filter(([kind]) => kind === 'run').length, 1);
});

test('chooses newest trusted artifact independently of response ordering', async () => {
  const mock = fixture([[artifact(2), artifact(9), artifact(5)]]);
  assert.deepEqual(await mock.find(), { runId: 9, artifactId: 9 });
});

for (const [description, change] of [
  ['wrong workflow', { workflow_id: 8 }],
  ['running workflow', { status: 'in_progress' }],
  ['failed workflow', { conclusion: 'failure' }],
  ['pull request', { event: 'pull_request' }],
  ['pull request target', { event: 'pull_request_target' }],
  ['non-main branch', { head_branch: 'feature' }],
  ['fork head', { head_repository: { full_name: 'fork/papers' } }],
  ['different repository', { repository: { full_name: 'owner/other' } }],
  ['mismatched commit', { head_sha: 'another-commit' }],
  ['mismatched run', { id: 100 }],
]) {
  test(`rejects ${description} and finds older trusted publication`, async () => {
    const mock = fixture([[artifact(9), artifact(2)]], { 9: run(9, change) });
    assert.deepEqual(await mock.find(), { runId: 2, artifactId: 2 });
  });
}

test('expired, fork and malformed artifact metadata never authorize a run', async () => {
  const fork = artifact(3);
  fork.workflow_run.head_repository_id = 11;
  const mock = fixture([[
    artifact(1, { expired: true }), fork,
    artifact(4, { workflow_run: null }), artifact(5, { expired: null }),
    artifact(6, { name: 'unrelated' }),
  ]]);
  assert.equal(await mock.find(), null);
  assert.deepEqual(mock.calls.map(([kind]) => kind), ['artifacts']);
});

test('no retained artifacts leaves static discovery intact', async () => {
  assert.equal(await fixture([[]]).find(), null);
});

test('exhausting the bounded artifact listing is an explicit failure', async () => {
  const page = Array.from({ length: 100 }, (_, i) => artifact(i + 1));
  const mock = fixture(Array.from({ length: 10 }, () => page));
  await assert.rejects(mock.find(), /pagination limit reached/);
  assert.equal(mock.calls.length, 10);
});

test('run verification has a hard request limit', async () => {
  const artifacts = Array.from({ length: 101 }, (_, i) => artifact(i + 1));
  const runs = Object.fromEntries(artifacts.map(a => [a.id, run(a.id, { conclusion: 'failure' })]));
  const mock = fixture([artifacts.slice(0, 100), artifacts.slice(100)], runs);
  await assert.rejects(mock.find(), /verification limit reached/);
  assert.equal(mock.calls.filter(([kind]) => kind === 'run').length, 100);
});

test('API failure propagates instead of authorizing unverified discovery', async () => {
  const github = { rest: { actions: {
    async listArtifactsForRepo() { throw new Error('503 unavailable'); },
  } } };
  await assert.rejects(
    findApiDiscovery({ github, owner: 'owner', repo: 'papers' }),
    /503 unavailable/,
  );
});
