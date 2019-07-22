#!/usr/bin/python

import sys

def rps(n, rnds=None, rnd=None):
    if rnds is None:
        rnds = []
    if rnd is None:
        rnd = []

    choices = ['rock', 'paper', 'scissors']

    for choice in choices:
        if len(rnd + [choice]) == n:
            rnds += [rnd + [choice]]
        else:
            rnds = rps(n, rnds, rnd + [choice])

    return rnds


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    return rps(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
       print('Usage: rps.py [num_plays]')
