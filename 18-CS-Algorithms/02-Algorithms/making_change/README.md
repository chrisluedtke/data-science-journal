# Making Change

You work as a bank teller, handling people's bank transactions. One day one of the wealthiest and also most eccentric patrons of the bank walks up to your stall. They hand you some cash and tell you they want you to figure out exactly how many ways there are to make change for the amount of money they plopped down in front of you using only pennies, nickels, dimes, quarters, and half-dollars. 

Since this is a bank, you have an infinite supply of coinage. Write a function `making_change` that receives as input an amount of money in cents as well as an array of coin denominations and calculates the total number of ways in which change can be made for the input amount using the given coin denominations. 

For example, `making_change(10)` should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

 1. We can make change for 10 cents using 10 pennies
 2. We can use 5 pennies and a nickel
 3. We can use 2 nickels
 4. We can use a single dime

## Testing 

For this problem, there's a test that tests your implementation with small inputs (amounts of change up to 300 cents). There's also a separate test that tests your implementation with large inputs (amounts of change >= 350 cents). 

You'll find that without implementing performance optimizations into your solution, your solution will likely hang on the large input test. 

To run the tests separately, run `python test_making_change.py -k small` in order to run just the small input test. Run `python test_making_change.py -k large` to execute just the large input test. If you want to run both tests, just run `python test_making_change.py`.

You can also test your implementation manually by executing `python making_change.py [amount]`

## Hints

 * This problem can be thought of as a more difficult version of the climbing stairs problem. 
 * As far as base cases go, again, think about some cases where we'd want the recursion to stop executing. What should happen when the amount of cents given is 0? What should happen when the amount of cents given is negative? What about when we've used up all of the available coin denominations?
 * As far as performance optimizations go, caching/memoization might be one avenue we could go down. 
 * Building up values in our cache in an iterative fashion might also be a good way to go about improving our implementation. 
 
   Here's a general idea: we can initialize a cache as a list (a dictionary would work fine as well) of 0s with a length equal to the amount we're looking to make change for. Each value of the list will represent the number of ways to make `i` cents, where `i` are the indices of the list. So `cache[10] == 4` from our example above. Since we know there is one way to make 0 cents in change, we'll initialize `cache[0] = 1` (you can seed entries for additional values as well, though you don't actually need to). 

   Now that we've initialized our cache, we'll start building it up. We have an initial value in our cache, so we'll want to build up subsequent answers in terms of this initial value. So, for a given coin, we can loop through all of the higher amounts between our coin and the amount (i.e., `for higher_amount in range(coin, amount + 1)`). If we take the difference between the higher amount and the value of our coin, we can start building up the values in our cache. 

   To go into a little more detail, let's walk through a small example. If we imagine our coin is a penny, in the first loop iteration, `higher_amount` is going to be 1 (since it will at first be the same value as our coin). If we take the difference between `higher_amount` and our coin value, we get 0. We already have a value for 0 in our cache; it's 1. So now we've just figured out 1 way to 1 cent from a penny. Add that answer to our cache. 

   Next up, on the next iteration, `higher_amount` will now be 2. The difference between `higher_amount` and our coin value now is 1. Well we just figured out an answer for 1, so now we have an answer for 2. Add that to our cache. 

   Once this loop finishes, we'll have figured out all of the ways to make different amounts using the current coin. At that point, all we have to do is perform that loop for every single coin, and then return the answer in our cache for the original amount!
