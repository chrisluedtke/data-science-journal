# Rock Paper Scissors

Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round. 

For example, given n = 2, your function should output the following:

```python
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]
```

Your output should be a list of lists containing strings. Each inner list should have length equal to the input n.

## Testing

Run the test file by executing `python test_rps.py`.

You can also test your implementation manually by executing `python rps.py [n]`.

## Hints

 * You'll want to define a list with all of the possible Rock Paper Scissors plays.
 * Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again. Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that each recursive call can add to the overall result. However, the tests only give our function `n` as input. To get around this, we could define an inner recursive helper function that will perform the recursion for us, while allowing us to preserve the outer function's function signature. 
 * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
 * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.