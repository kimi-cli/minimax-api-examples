#!/usr/bin/env python3
"""Chat with MiniMax M3 through the Anthropic-compatible text API.

The platform docs file the text API under text-anthropic-api, so the
standard anthropic client works with a custom base URL.

Env:
  MINIMAX_API_KEY   your MiniMax platform key
  MINIMAX_BASE_URL  base URL from the text API reference page
"""
import os
import sys

import anthropic

# Model name as listed in the platform model table.
# Alternatives: MiniMax-M2.7, MiniMax-M2.7-highspeed, MiniMax-M2.5
MODEL = os.environ.get('MINIMAX_MODEL', 'MiniMax-M3')


def ask(prompt: str) -> str:
    client = anthropic.Anthropic(
        api_key=os.environ['MINIMAX_API_KEY'],
        base_url=os.environ['MINIMAX_BASE_URL'],
    )
    message = client.messages.create(
        model=MODEL,
        max_tokens=1024,  # illustrative; see the reference for limits
        messages=[{'role': 'user', 'content': prompt}],
    )
    return ''.join(block.text for block in message.content if hasattr(block, 'text'))


def main() -> None:
    prompt = ' '.join(sys.argv[1:]) or 'Write a Python function that parses ISO 8601 dates.'
    print(ask(prompt))


if __name__ == '__main__':
    main()
