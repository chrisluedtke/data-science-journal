#!/usr/bin/python

def fib1(n):  # O(2 ^ n)
    if n < 2:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n, cache=dict()):  # O(n)
    if n < 2: 
        return n
    elif n in cache:
        return cache[n]
    else:
        cache[n] = fib2(n - 1, cache) + fib2(n - 2, cache)
        return cache[n]


if __name__ == '__main__':
    print(fib1(8))
    print(fib2(8))
