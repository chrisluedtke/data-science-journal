# Sprint Challenge: Algorithms

In this week's Sprint you explored and implemented some classic algorithmic approaches and used them to solve novel problems. You also implemented some classic and fundamental sorting algorithms and learned about how to go about evaluating their respective runtimes and performance. This Sprint Challenge aims to assess your comfort with these topics through exercises that build on the algorithmic intuition you've started to build up.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your Challenge score is a measure of your ability to work independently using the material covered throughout this sprint. You need to demonstrate proficiency in the
concepts and objectives that were introduced and that you practiced in the preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and
Instructor in your cohort help channel on Slack. Your submitted work reflects your proficiency in the concepts and topics that were covered this week.

You have three hours to complete this Sprint Challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons) and it also helps your project manager to more thoroughly assess your work.

## Description

This Sprint Challenge is split into two separate parts that test your ability to write and analyze algorithms.

### 1. Short Answer Questions (30 points)

 > It is recommended that you spend no more than 1 hour on this portion of the Sprint Challenge.

For this portion of the Sprint Challenge, you'll be answering questions posed in the `Algorithms_Questions.md` document. Write down your answer and also write down a justification for _why_ you put down that answer. This could net you some partial credit if your justification is sound but the answer you put down turns out to not be correct.

### 2. Implement Robot Sort (60 points)

You have been given a robot with very basic capabilities:

  * It can move left or right.
  * It can pick up an item
    * If it tries to pick up an item while already holding one, it will swap the items instead.
  * It can compare the item it's holding to the item in front of it.
  * It can switch a light on its head on or off.

Your task is to program this robot to sort lists using ONLY these abilities.

#### Rules

Inside the `Robot_Sort` directory you'll find the `robot_sort.py` file. Open it up and read through each of the robot's abilities. Once you've understood those, start filling out the `sort()` method following these rules:

  * You may use any pre-defined robot methods.
  * You may NOT modify any pre-defined robot methods.
  * You may use logical operators. (`if`, `and`, `or`, `not`, etc.)
  * You may use comparison operators. (`>`, `>=`, `<`, `<=`, `==`, `is`, etc.)
  * You may use iterators. (`while`, `for`, `break`, `continue`)
  * You may NOT store any variables. (`=`)
  * You may NOT access any instance variables directly. (`self._anything`)
  * You may NOT use any Python libraries or class methods. (`sorted()`, etc.)
  * You may define robot helper methods, as long as they follow all the rules.

#### Hints

* Make sure you understand the problem and all of the rules! A solution that breaks the rules will receive no credit.

* If you're unsure if an operator or method is allowed, ask.

* Lay out some numbered cards in a line and try sorting them as if you were the robot.

* Come up with a plan and write out your algorithm before coding. If your plan is sound but you don't reach a working implementation in three hours, you may receive partial credit.

* There is no efficiency requirement but you may lose points for an unreasonably slow solution. Tests should run in far less than 1 second.

* We discussed a sorting method this week that might be useful. Which one?

* The robot has exactly one bit of memory: its light. Why is this important?

Run `python test_robot.py` to run the tests for your `robot sort` function to ensure that your implementation is correct.

### Stretch (8 points)

Uncomment the `test_stretch_times()` test in `test_robot.py`. Can you optimize your robot sort to perform better than the given times?

## Grading Rubric

* *1*: 0-69
* *2*: 70-89
* *3*: 90+
