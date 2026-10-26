'use strict';

// Filter artifacts, not recent runs: successful probes do not publish discovery.
// Bound API work and fail closed if the listing cannot be examined completely.
const ARTIFACT_NAME = 'agent-api-discovery';
const MAX_PAGES = 10;
const MAX_RUN_CHECKS = 100;
const PAGE_SIZE = 100;

async function findApiDiscovery({ github, owner, repo }) {
  const artifacts = [];
  let complete = false;
  for (let page = 1; page <= MAX_PAGES; page++) {
    const response = await github.rest.actions.listArtifactsForRepo({
      owner, repo, name: ARTIFACT_NAME, per_page: PAGE_SIZE, page,
    });
    const rows = response.data.artifacts;
    if (!Array.isArray(rows)) throw new Error('Invalid discovery artifact listing');
    artifacts.push(...rows);
    if (rows.length < PAGE_SIZE) {
      complete = true;
      break;
    }
  }
  if (!complete) throw new Error('Discovery artifact pagination limit reached');

  const candidates = artifacts.filter(artifact => (
    artifact.name === ARTIFACT_NAME && artifact.expired === false
    && Number.isSafeInteger(artifact.id)
    && Number.isSafeInteger(artifact.workflow_run?.id)
    && artifact.workflow_run.head_branch === 'main'
    && Number.isSafeInteger(artifact.workflow_run.repository_id)
    && artifact.workflow_run.repository_id === artifact.workflow_run.head_repository_id
  )).sort((a, b) => b.id - a.id);
  if (candidates.length === 0) return null;

  const expected = await github.rest.actions.getWorkflow({
    owner, repo, workflow_id: 'agent-api.yml',
  });
  if (!Number.isSafeInteger(expected.data.id)) {
    throw new Error('Invalid Agent API workflow identity');
  }
  const runs = new Map();
  for (const artifact of candidates) {
    const runId = artifact.workflow_run.id;
    if (!runs.has(runId)) {
      if (runs.size >= MAX_RUN_CHECKS) {
        throw new Error('Discovery run verification limit reached');
      }
      const response = await github.rest.actions.getWorkflowRun({
        owner, repo, run_id: runId,
      });
      runs.set(runId, response.data);
    }
    const run = runs.get(runId);
    if (run.id !== runId || run.workflow_id !== expected.data.id
        || run.status !== 'completed' || run.conclusion !== 'success'
        || !['push', 'workflow_dispatch'].includes(run.event)
        || run.head_branch !== 'main'
        || run.head_repository?.full_name !== `${owner}/${repo}`
        || run.repository?.full_name !== `${owner}/${repo}`
        || run.head_sha !== artifact.workflow_run.head_sha) continue;
    return { runId, artifactId: artifact.id };
  }
  return null;
}

module.exports = { findApiDiscovery };
