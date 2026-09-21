#!/usr/bin/env python3
"""Send one chat message to MiniMax M3 through OpenRouter.

Env:
  OPENROUTER_API_KEY   your OpenRouter key
  OPENROUTER_BASE_URL  base URL from the OpenRouter quickstart
"""
import os
import sys

import requests

# Slug from the OpenRouter MiniMax provider page.
MODEL = os.environ.get('OPENROUTER_MODEL', 'minimax/minimax-m3')


def ask(prompt: str) -> str:
    base = os.environ['OPENROUTER_BASE_URL'].rstrip('/')
    resp = requests.post(
        f'{base}/chat/completions',  # path per the OpenRouter quickstart; confirm there
        headers={'Authorization': 'Bearer ' + os.environ['OPENROUTER_API_KEY']},
        json={
            'model': MODEL,
            'messages': [{'role': 'user', 'content': prompt}],
        },
        timeout=120,
    )
    resp.raise_for_status()
    body = resp.json()
    return body['choices'][0]['message']['content']


def main() -> None:
    prompt = ' '.join(sys.argv[1:]) or 'Explain sparse attention in three sentences.'
    print(ask(prompt))


if __name__ == '__main__':
    main()
