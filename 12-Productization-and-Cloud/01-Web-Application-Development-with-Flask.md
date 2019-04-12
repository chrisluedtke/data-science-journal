# Web Application Development with Flask

In the modern day, most applications we interact with are *web* applications -
client-server architectures delivered via HTTP and accessed with a web browser.
As a data scientist we will generally not build such applications, but we do
have to *understand* them and their components.

## Learning Objectives

- Distinguish between front-end, back-end, database, and what tasks are
  appropriate for which
- Create a simple Python web application that exposes an API to URL endpoints

## Before Lecture

Read up on [Flask](http://flask.pocoo.org/), a "microframework" for developing
web applications. All this really means is that it's small and modular, and
mostly just provides for URL routing and responses - for other things
(templates, database, forms) you pick and choose your own other packages (and
we'll give you some specific choices for this week).

This is in contrast with [Django](https://www.djangoproject.com/), the most
popular "industry-grade" Python web application framework. Django is
*opinionated*, and comes with built-in modules for pretty much everything.

There are more projects built with Django than Flask, but Flask is solidly
second place in the Python web application ecosystem, and is a better minimal
choice for a data scientist who just wants to get some results.

## Live Lecture Task

We're going to kick off with an overview of the major parts of a web application
(front-end, back-end, database), and then develop our own prototype web
application using Flask and SQLite. A summary of the overall picture:

- Front-end: the "look-and-feel" of an application, as well as any logic that is
  executed by client-side (browser) JavaScript (which has grown surprisingly
  powerful)
- Back-end: the routing and "business logic", where responses
  (what the client sees) are built and APIs and databases are accessed
- Database: the "source of truth", where data is persisted and updated

## Assignment

- Reproduce the steps from lecture: write and run a basic local Flask web
  application
- Create a model for `Tweet` and `User` as demonstrated in lecture, and populate
  your local (SQLite) database with some invented data (at least 6 Tweets and 2
  Users)
- For tomorrow, make sure to sign up for the [Twitter Developer
  API](https://developer.twitter.com/en/apply-for-access) and
  [Basilica](https://www.basilica.ai/), as we will use both APIs in our
  application to get more and real data!

## Resources and Stretch Goals

- [Jinja2](http://jinja.pocoo.org/) is the dominant template engine, which you
  will use to build the look and layout of the pages in your application
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) is an ORM
  (object-relational mapping), and will let us both (a) not have to write SQL,
  and (b) use OOP to interact with data with multiple backends (SQLite locally,
  and PostgreSQL in the cloud)
- [SQLAlchemy Data
  Types](https://docs.sqlalchemy.org/en/latest/core/type_basics.html) are needed
  to build usable models that will translate to SQL
- Making the front-end look nice is very much a stretch goal throughout this
  sprint - but if you are interested in it, [Picnic CSS](https://picnicss.com/)
  and [Umbrella JS](https://umbrellajs.com/) are nice lightweight and modern
  tools (alternatives to Bootstrap and JQuery respectively)
- Experiment with SQLAlchemy models - you can add more fields of interest to the
  `Tweet` and `User` models and/or add different models for other purposes
