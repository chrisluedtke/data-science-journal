#!/usr/bin/python

import sys

def making_change(amount, denominations):
    cache={0:1}

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            if higher_amount not in cache:
                cache[higher_amount] = 0
            if higher_amount-coin >= 0:
                cache[higher_amount] += cache[higher_amount-coin]

    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        ways = making_change(amount, denominations)
        print(f"There are {ways} ways to make {amount} cents.")
    else:
        print("Usage: making_change.py [amount]")


# 0   1  
# 1   1  [ 1p]
# 2   1  [ 2p]
# 3   1  [ 3p]
# 4   1  [ 4p]
# 5   2  [ 5p] [   , 1n]
# 6   2  [ 6p] [ 1p, 1n]
# 7   2  [ 7p] [ 2p, 1n]
# 8   2  [ 8p] [ 3p, 1n]
# 9   2  [ 9p] [ 4p, 1n]
# 10  4  [10p] [ 5p, 1n] [   , 2n] [   ,   , 1d]
# 11  4  [11p] [ 1p, 1n] [ 1p, 2n] [ 1p,   , 1d]
# 12  4  [12p] [ 7p, 1n] [ 2p, 2n] [ 2p,   , 1d]


def list_arg(l=[]):
    l.append(2)
    print(l)
    return None