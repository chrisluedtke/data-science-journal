# Object-Oriented Programming, Code Style and Reviews

"Code that works" is good - "code that other people can read" is better.

## Learning Objectives

- create a basic Python class, with a constructor, methods, and fields
- write stylistic (PEP 8) Python code, and give and receive a basic code review

## Before Lecture

Read the [official Python Class
tutorial](https://docs.python.org/3/tutorial/classes.html), and try to reproduce
the examples in your own Python environment.

Read the [PEP 8 style guide](https://pep8.org/), and then look back at code
you've written in the past. Identify at least three times you did something the
style guide says you shouldn't, and write the corrected version.

## Live Lecture Task

We will first live code a class based on class request/discussion, brainstorming
what fields and methods make sense. We will then discuss style more broadly.

Style matters - but we're engineers, which means we're a little lazy. Let's set
up tools to check style automatically, so we fix issues before they hit review.

Then we will discuss what a code review actually is, and if folks are brave they
can volunteer to have their code reviewed with the class. It's scary, but this
is a safe time to do it (and good practice for the assignment!).

## Assignment

First, revisit your code from yesterday - was it stylistic? Run a style check
(as shown in lecture) and correct any issues you see. Also, refactor your code
to use at least 1 class - remember, be DRY (Don't Repeat Yourself), not WET
(Write Every Time)!

Then - code review! Pair with another student (PMs will facilitate, especially
in case of odd numbers), and share your `lambdata` repo with each other. Read
and review their code, and also check that they have published their package to
test PyPI and that it can be installed and used.

Read the [Lambda School Peer Code Review
Checklist](https://github.com/LambdaSchool/Peer-Code-Review-Checklist)
and [fill out the review form](https://airtable.com/shrVBzrhkcT6GqExr) for your
peer.

The objectives to evaluate are as described in the prior module (`lambdata`
package with at least 2 helper functions, published on test PyPI). If they meet
the requirements it is a 2, exceed is a 3, and don't meet is a 1.

Considerations to keep in mind while doing a code review:
- Can you follow the code flow/layout?
- Can you understand the logic/reasoning for what it is doing?
- Could you build with (`import` and use) or extend on it (as a developer adding
  more to the codebase)?

For comments and notes, focus on style and design. Find at least *2* things to
compliment and at least *1* constructive criticism. It's also great to learn
things from their code, and ask questions if there's something you don't
understand. Good code isn't clever - it's clear!

## Resources and Stretch Goals

If you have trouble getting a PEP8 tool working in your local environment, you
can use [PEP8 online](http://pep8online.com/) to check code.

Also, many organizations create their own "flavor" of style guides - for an example,
read the
[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

And if you get through all the above - make `lambdata` better! Implement 2 more
helper functions, and/or refactor your code to be more object-oriented.
