# Sprint Challenge: Data Structures

In this week's Sprint you implemented some classic and fundamental data structures and learned about how to go about evaluating their respective runtimes and performance. This Sprint Challenge aims to assess your comfort with these topics through exercises that build on the data structures you implemented and the algorithmic intuition you've started to build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge score is a measure of your ability to work independently using the material covered throughout this sprint. You need to demonstrate proficiency in the concepts and objectives that were introduced and that you practiced in the preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your submitted work reflects your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons) and it also helps your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into three parts:

1. Implement a data structure called a ring buffer (more details below)
2. Optimizing some inefficient code
3. Analyzing time and space complexities from parts 1 and 2

### Minimum Viable Product

#### Task 1. Implement a Ring Buffer Data Structure

A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

For example:

```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
```

#### Task 2. Runtime Optimization

Navigate into the `names` directory. Here you will find two text files containing 10,000 names each, along with a program `names.py` that compares the two files and prints out duplicate name entries. Try running the code with `python3 names.py`. Be patient because it might take a while: approximately six seconds on my laptop. What is the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the code. Can you get the runtime to under a second? Under one hundredth of a second?

(Hint: You might try importing a data structure you built during the week)

#### Task 3. Analyze Some Runtimes

Open up the `Data_Structures_Answers.md` file. This is where you'll jot down your answers for the runtimes of the functions/data structures you just implemented. Also include the runtime and space complexities of the original code and your optimized solution from `names.py`.

### Stretch Problems

1. Say your code from `names.py` is to run on an embedded computer with very limited RAM. Because of this, memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists). How would you go about optimizing the code under these conditions? Try it out and compare your solution to the original runtime. (If this solution is less efficient than your original solution, include both and label the strech solution with a comment)


### Rubric

#### Ring Buffer

- Ring buffer implementation passes the tests: 10 points total

#### Names

- Optimize with an O(n log n) runtime solution: 8 points total
- Optimize with an O(n) runtime solution: 10 points total

#### Complexity

- One point each: 8 points total

#### Stretch

- `names.py` is optimized with sub-quadratic runtime complexity and tightly constrained linear space complexity: 4 points


#### Grading

* *3*: 28+
* *2*: 20-27
* *1*: 0-19
