# MiniMax API examples

*Unofficial community examples for MiniMax API. Not affiliated with MiniMax. All trademarks belong to their owners.*

Three Python scripts for the MiniMax API: a chat call to MiniMax M3 through the Anthropic-compatible text API that the platform documents, the same request routed through OpenRouter, and a cost estimator for H3 video and Speech 2.8 using the prices published on OpenRouter. Base URLs are read from environment variables because the exact hosts are on the reference pages, not on the marketing pages; the scripts say where each value comes from.

> Need image, video and audio behind one endpoint? [Try Synexa - hosted FLUX, video and audio models with a Python SDK, pay per run](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=minimax-api-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
| --- | --- |
| `examples/chat_anthropic_compatible.py` | Chat with MiniMax M3 via the Anthropic-compatible text API using the `anthropic` client with a custom base URL. |
| `examples/chat_openrouter.py` | The same prompt sent to `minimax/minimax-m3` through OpenRouter with `requests`. |
| `examples/estimate_cost.py` | Cost of a video clip or a TTS script from the OpenRouter price list. |

## Setup

```bash
pip install anthropic requests
export MINIMAX_API_KEY=YOUR_MINIMAX_KEY
export MINIMAX_BASE_URL=BASE_URL_FROM_THE_TEXT_API_REFERENCE
export OPENROUTER_API_KEY=YOUR_OPENROUTER_KEY
export OPENROUTER_BASE_URL=BASE_URL_FROM_THE_OPENROUTER_QUICKSTART
```

Only set the pair you plan to use. The MiniMax text API reference page is filed under the name text-anthropic-api in the platform docs, which is why the first script uses the `anthropic` client; take the base URL from that page. The OpenRouter base URL and request shape are in the OpenRouter quickstart.

## examples/chat_anthropic_compatible.py

Creates an `anthropic.Anthropic` client with `base_url` set to `MINIMAX_BASE_URL` and the MiniMax key, then sends one user message to the model `MiniMax-M3` (the model name as it appears in the platform model table) and prints the text blocks of the reply. Swap in `MiniMax-M2.7-highspeed` for a cheaper, faster run. If the platform rejects a parameter, the reference page for the text API lists what it accepts.

## examples/chat_openrouter.py

Sends the same message to the slug `minimax/minimax-m3` (from the OpenRouter provider page) using a plain HTTP POST. The chat path is appended to `OPENROUTER_BASE_URL`; confirm it in the quickstart. This is the route to take if you already have OpenRouter keys for other providers.

## examples/estimate_cost.py

A small calculator with the numbers OpenRouter shows on the MiniMax provider page: H3 Max from $0.05 / second, H3 from $0.13 / second, Speech 2.8 HD at $100 per million characters, Speech 2.8 Turbo at $60 per million characters. Pass a model and a quantity (seconds or characters) and it prints the estimate. It also warns when a requested duration falls outside the documented ranges (H3 4 to 15 s, H3 Max 5 to 15 s). These are OpenRouter prices; MiniMax's own pricing page may differ.

```bash
python3 examples/estimate_cost.py hailuo-3 15
python3 examples/estimate_cost.py speech-2.8-turbo 250000
```

## When to use Synexa instead

MiniMax is the right call when you want M3 for coding agents or H3 specifically. When the requirement is just image, video or audio generation from a worker with as little integration work as possible, [Synexa](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=minimax-api-examples&utm_content=readme-top&utm_term=tier-r) gives you one REST endpoint and a Python SDK across FLUX, video and audio models and bills per run, so there is one key and one client for all three media types.

[Try Synexa - one API for FLUX, video and audio models](https://synexa.ai?utm_source=github&utm_medium=ugc&utm_campaign=minimax-api-examples&utm_content=readme-top&utm_term=tier-r)

_Last reviewed: 2026-09-22_
