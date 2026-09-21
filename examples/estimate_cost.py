#!/usr/bin/env python3
"""Estimate MiniMax video or speech cost from the OpenRouter price list.

Prices are the ones shown on the OpenRouter MiniMax provider page at the
time of writing, not MiniMax's own pricing page. Re-check before use.

Usage: python3 estimate_cost.py MODEL QUANTITY
  video models take seconds, speech models take characters
"""
import sys

# key: (unit, usd per unit, (min, max) documented range or None)
PRICES = {
    'hailuo-3': ('second', 0.13, (4, 15)),        # MiniMax H3, 768P / 2K
    'hailuo-3-max': ('second', 0.05, (5, 15)),    # MiniMax H3 Max, 480P / 768P
    'speech-2.8-hd': ('character', 100 / 1_000_000, None),
    'speech-2.8-turbo': ('character', 60 / 1_000_000, None),
}


def estimate(model: str, quantity: float) -> float:
    return quantity * PRICES[model][1]


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in PRICES:
        print('usage: estimate_cost.py MODEL QUANTITY')
        print('models: ' + ', '.join(PRICES))
        sys.exit(2)
    model, quantity = sys.argv[1], float(sys.argv[2])
    unit, _, span = PRICES[model]
    cost = estimate(model, quantity)
    print(f'{model}: {quantity:g} {unit}s -> ${cost:.4f}')
    if span and not (span[0] <= quantity <= span[1]):
        print(f'  warning: documented duration range is {span[0]} to {span[1]} s')


if __name__ == '__main__':
    main()
