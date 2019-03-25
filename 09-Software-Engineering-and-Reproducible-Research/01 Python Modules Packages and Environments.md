# Python Modules, Packages, and Environments

Places for your code (and dependencies) to live.

## Learning Objectives

- Understand and follow Python namespaces and imports
- Create a Python package and install dependencies in a dedicated environment

## Before Lecture

Install [Anaconda](https://www.anaconda.com/distribution) on your local machine
if you haven't already, and read the official documentation for
[Python modules](https://docs.python.org/3.7/tutorial/modules.html).

## Live Lecture Task

We're going to start our own Python package the right way - by making an
environment with `pipenv`, installing our dependencies, and making some classes.

## Assignment

1) Create your own `lambdata-yourusername` package, as shown in lecture
2) Implement at least 2 of the following "helper" utility functions:
  - Check a dataframe for nulls, print/report them in a nice "pretty" format
  - Report a confusion matrix, with labels for easier interpretation
  - Train/*validate*/test split function for a dataframe
  - "Generate more data" function, takes dataframes and makes more rows
  - Contingency table + Chi-squared report function: takes two categorical
    variables, outputs a contingency table and corresponding Chi-squared test
  - Split addresses into multiple columns city, state zip -> df['city]
    df['state'] df['zip'] use regexes to detect format and pull out important
    pieces
  - State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
    (Handle Washington DC and territories like Puerto Rico etc.)
  - Single function to take a list, turn it into a series and add it to a
    dataframe as a new column
  - 1.5*Interquartile range outlier detection/removal function.
  - Function to set notebook display options.
  - Function to split dates ("MM/DD/YYYY", etc.) into multiple columns
  - Your idea here! (You will implement more later in the week as well)
3) Register for a [test PyPI account](https://test.pypi.org/account/register/)
4) Publish your package as `lambdata-yourusername` (to avoid conflicts)
5) Start a Python notebook, and install your package with
  `!pip install --index-url https://test.pypi.org/simple/ lambdata-yourusername`
6) `import lambdata-yourusername as lambdata` in your notebook, and try it out!

We'll step through in lecture - building and publishing a package requires
`twine`, and is generally done with these commands:
- `python setup.py sdist bdist_wheel` (build the actual package)
- `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

`twine` itself can be installed with `pipenv install -d twine` so it is a
development dependency.

Many of the utility functions can be implemented with the right clever calls
to `pandas`, `numpy`, and other libraries - that's fine! Use those as
dependencies. There's still value in a package that encapsulates more
complicated libraries and exposes streamlined functionality with a simplified
API.

Also note - there's a lot more than 2 ideas above. Throughout the week, whenever
you have finished the daily assignment baseline, you can always come back and
add more functionality to your `lambdata` (including ideas of your own)!

## Resources and Stretch Goals

The [official Python packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/)
can help you if you get stuck with the assignment. Make sure to use Test PyPI!
If you get through all the steps, try some of the following stretch goals:

- Check out the source code for [pandas](https://github.com/pandas-dev/pandas),
  and see if you can make sense of it. Try to find the actual logic behind
  specific functions you use (e.g. `pd.DataFrame`, `df.replace`, etc.). Reading
  source code is challenging, especially from large codebases, but it's a skill
  that will help you debug and fix real issues in professional situations.

- Explore [PyPI](https://pypi.org), the Python Package Index - this is where
  `pip` (the official base Python package installer, which both Anaconda and
  `pipenv` build on) gets things from by default. For now stick with Test PyPI
  for your own publishing, but you can work to make things "real"!
