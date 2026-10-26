'''Delete one uniquely named probe without inspecting unrelated KV storage.'''

import argparse
import http.client
import json
import os
import re
import time
import urllib.error
import urllib.request


def delete_probe(name):
    pattern = r'key-papers-static-probe-[1-9][0-9]*-[1-9][0-9]*'
    if not re.fullmatch(pattern, name):
        raise ValueError('Only a run-specific static probe may be deleted')
    account = os.environ.get('CLOUDFLARE_ACCOUNT_ID', '')
    token = os.environ.get('CLOUDFLARE_API_TOKEN', '')
    if not re.fullmatch(r'[a-fA-F0-9]{32}', account) or not token:
        raise ValueError('Cloudflare credentials are missing or malformed')
    request = urllib.request.Request(
        f'https://api.cloudflare.com/client/v4/accounts/{account}'
        f'/workers/scripts/{name}', method='DELETE',
        headers={'authorization': f'Bearer {token}'})
    for attempt in range(3):
        try:
            try:
                response = urllib.request.urlopen(request, timeout=20)
            except urllib.error.HTTPError as exc:
                response = exc
            with response:
                status = response.status
                text = response.read().decode()
            try:
                body = json.loads(text) if text.strip() else {}
            except ValueError:
                body = None
            errors = body.get('errors') if isinstance(body, dict) else None
            no_errors = errors is None or errors == []
            if (200 <= status < 300 and isinstance(body, dict)
                    and (not text.strip() or body.get('success') is True)
                    and no_errors):
                return 'deleted'
            codes = []
            if isinstance(errors, list):
                codes = [error['code'] for error in errors
                         if isinstance(error, dict)
                         and type(error.get('code')) is int]
            # Null/malformed errors are not affirmative evidence of absence.
            # Every entry must contain a recognized integer code; do not hide
            # unknown entries by filtering them out of the diagnostic list.
            if (status == 404 and codes and len(codes) == len(errors)
                    and set(codes) <= {10007, 10090}):
                return 'already absent'
            message = f'Probe deletion HTTP {status}; error codes: {codes}'
            if status != 429 and status < 500:
                raise ValueError(message)
        except (OSError, http.client.HTTPException) as exc:
            message = 'Probe deletion network error: ' + type(exc).__name__
        if attempt < 2:
            time.sleep(attempt + 1)
    raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name')
    args = parser.parse_args()
    try:
        result = delete_probe(args.name)
    except ValueError as exc:
        parser.exit(1, str(exc) + '\n')
    print(f'{args.name}: {result}')


if __name__ == '__main__':
    main()
