#!/usr/bin/python

import argparse

def find_max_profit(prices):   # O(n ^ 2)
    profit = None
    for i, val_1 in enumerate(prices):
        for val_2 in prices[i+1:]:
            cand = val_2 - val_1
            if profit is None or cand > profit:
                profit = cand

    return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', 
                        help='an integer price')
    args = parser.parse_args()
    profit = find_max_profit(args.integers)
    prices = args.integers
    print(f"A profit of ${profit} can be made from the stock prices {prices}.")