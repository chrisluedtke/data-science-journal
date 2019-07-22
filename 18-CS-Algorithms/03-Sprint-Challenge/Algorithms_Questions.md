# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

1.
    ```python
    a = 0
    while (a < n * n * n):
        a = a + n * n
    ```
    > `O(n ^ 3) / O(n ^ 2)`, or `O(n)`.
2.
    ```python
    sum = 0
    for i in range(n):
        i += 1
        for j in range(i + 1, n):
            j += 1
            for k in range(j + 1, n):
                k += 1
                for l in range(k + 1, 10 + k):
                    l += 1
                    sum += 1
    ```
    > `O(n ^ 3)`. The last loop is a bit tricky - it will add `10 * n` operations. In reality we would not run `n ^ 3` operations, but that's what we converge to at large `n`.
3.
    ```python
    def bunnyEars(bunnies):
        if bunnies == 0:
            return 0

        return 2 + bunnyEars(bunnies-1)
    ```
    > `O(n)`

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the runtime complexity of your solution.

> * Considering all floors, drop an egg from of the middle floor
>   * If egg breaks, reduce the floors we consider to the bottom half of the floors in our current consideration. Repeat the previous step.
>   * If egg does not break, reduce the floors we consider to the top half of the floors in our current consideration. Repeat the previous step.
> * Repeat the above process, keeping track of the results at each floor, until we find a floor at which the egg does not break and a (floor + 1) at which it does break.
> 
> This is an `O(log(n))` solution, since we cut our maximum remaining operations in half at each iteration.