# Software Testing, Documentation, and Licensing

For code to stand the test of time, it is not enough to be well-written - it
must be tested and documented. It is also important to understand the basics of
software licensing, both in the code you depend on and create.

## Learning Objectives

- Understand purpose of and approaches towards software testing, and be able to
  write basic unit tests
- Read and write quality comments, Pydoc, and READMEs
- Recognize major open-source licenses and their significance for personal and
  professional use

## Before Lecture

Read the official documentation for
[unittest](https://docs.python.org/3/library/unittest.html), a Python module for
writing basic tests included in the standard library.

Read the [pandas
README.md](https://github.com/pandas-dev/pandas/blob/master/README.md) - it
strikes a good balance between skimmability, immediate usefulness, and reference
links for more details.

Check out the [Open Source Initiative](https://opensource.org/licenses), the
group that formally approves licenses as being "open source." You'll see some
familiar and less-familiar license names, as well as a [useful
FAQ](https://opensource.org/faq).

## Live Lecture Task

First we'll write some basic unit tests to demonstrate their functionality.
We'll apply these concepts to `lambdata`, but also discuss them more generally.
Come with questions and be prepared to discuss documentation and licensing as
well!

## Assignment

Spruce up `lambdata`!

- Add at least one basic `unittest` to `lambdata`
- Make sure there are docstrings wherever PEP 8 demands
- Write a high-quality `README.md` that is both skimmable and has appropriate
  examples/details/links for someone who wants to understand your code
- Pick a license for your package, and add it in a `LICENSE` file.

## Resources and Stretch Goals

Add a `ROADMAP.md` file to your repo, with an outline of where you'd like to
take your `lambdata` project. It can also include guidelines for what sort of
contributions you'd like to have and how somebody can go about getting started
building and developing on your code.

Run [pydoc](https://docs.python.org/3.7/library/pydoc.html) on your `lambdata`
package to generate documentation based on your docstring comments. Try browsing
it locally, and for an extra stretch goal - put it in a `/docs` directory in
your repo and enable GitHub Pages to serve it on the web!

Try [pytest](https://docs.pytest.org/en/latest/), a widely used Python testing
framework a bit more powerful than `unittest` (though you do have to install
it - but you've been dealing with `pip` a lot!).

Read [the MIT License, Line by
Line](https://writing.kemitchell.com/2016/09/21/MIT-License-Line-by-Line.html),
and write your own summary of it with a target audience of another person who
writes code..
