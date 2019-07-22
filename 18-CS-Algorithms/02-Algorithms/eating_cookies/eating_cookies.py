#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache={}):
    if n in cache:
        return cache[n]
    elif n == 0:  # or initialize cache={0:1}
        return 1
    elif n < 0:
        return 0
    else:
        cache[n] = sum([eating_cookies(n-_, cache) for _ in range(1, 4)])
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(f"There are {eating_cookies(num_cookies)} ways "
              f"for Cookie Monster to eat {num_cookies} cookies.")
    else:
        print('Usage: eating_cookies.py [num_cookies]')
