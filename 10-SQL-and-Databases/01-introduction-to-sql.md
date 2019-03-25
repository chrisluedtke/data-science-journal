# Introduction to SQL

The basics of Structured Query Language, a relatively simple query language.

## Learning Objectives

- Write basic SQL queries to get specific subsets of data from a database and
  answer basic "business questions"
- Understand the purpose of SQL join, and perform joins to access data from
  multiple tables

## Resources

* [sqlite3](https://docs.python.org/3/library/sqlite3.html), an API for data persistence via the SQLite - a simple disk-based database that doesn't require a separate server process. Read the tutorial, and try the given examples. See if you can modify them in simple ways, and come with questions!
* [DB Browser for SQLite](https://sqlitebrowser.org) - a helpful utility for ad hoc inspection and querying.
* [SQL Quick Reference from W3Schools](https://www.w3schools.com/SQL/sql_quickref.asp)
* [pandas.DataFrame.to_sql](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html)
* [pandas.read_sql_query](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_sql_query.html)

## Live Lecture Task

We'll work together with SQLite in Python, making and exploring a simple
database and trying a range of basic queries. Focus will be on the following SQL
keywords:

- `SELECT` - how we choose which columns to get
- `WHERE` - how we set conditions on the rows to be returned
- `LIMIT` - when we only want a certain number of rows
- `ORDER` - when we want to sort the output
- `JOIN` - when we need data from multiple tables combined

We'll also learn about how to use `CREATE TABLE` to specify a schema for our
data, and `INSERT` statements to put data into a table. And lastly, we'll learn
how to calculate some basic statistics with `COUNT()`, `AVG()`, and `SUM()`,
organized using the keyword `GROUP`.

## Assignment - Part 1, Querying a Database

This directory contains a file `rpg_db.sqlite3`, a database for a hypothetical
webapp role-playing game. This test data has dozens-to-hundreds of randomly
generated characters across the base classes (Fighter, Mage, Cleric, and Thief)
as well as a few Necromancers. Also generated are Items, Weapons, and
connections from characters to them. Note that, while the name field was
randomized, the numeric and boolean fields were left as defaults.

Use `sqlite3` to load and write queries to explore the data, and answer the
following questions:

- How many total Characters are there?
- How many of each specific subclass?
- How many total Items?
- How many of the Items are weapons? How many are not?
- How many Items does each character have? (Return first 20 rows)
- How many Weapons does each character have? (Return first 20 rows)
- On average, how many Items does each Character have?
- On average, how many Weapons does each character have?

You do not need all the tables - in particular, the `account_*`, `auth_*`,
`django_*`, and `socialaccount_*` tables are for the application and do not have
the data you need. the `charactercreator_*` and `armory_*` tables and where you
should focus your attention. `armory_item` and `charactercreator_character` are
the main tables for Items and Characters respectively - the other tables are
subsets of them by type (i.e. subclasses), connected via a key (`item_id` and
`character_id`).

You can use the DB Browser or other tools to explore the data and work on your
queries if you wish, but to complete the assignment you should write a file
`rpg_queries.py` that imports `sqlite3` and programmatically executes and
reports results for the above queries.

Some of these queries are challenging - that's OK! You can keep working on them
tomorrow as well (we'll visit loading the same data into PostgreSQL). It's also
OK to figure out the results partially with a query and partially with a bit of
logic or math afterwards, though doing things purely with SQL is a good goal.
[Subqueries](https://www.w3resource.com/sql/subqueries/understanding-sql-subqueries.php)
and [aggregation functions](https://www.sqltutorial.org/sql-aggregate-functions/)
may be helpful for putting together more complicated queries.

## Assigment - Part 2, Making and populating a Database

Load the data (use `pandas`) from the provided file `buddymove_holidayiq.csv`
(the [BuddyMove Data
Set](https://archive.ics.uci.edu/ml/datasets/BuddyMove+Data+Set)) - you should
have 249 rows, 7 columns, and no missing values. The data reflects the number of
place reviews by given users across a variety of categories (sports, parks,
malls, etc.).

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `buddymove_holidayiq.sqlite3`
- Use `df.to_sql`
  ([documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_sql.html))
  to insert the data into a new table `review` in the SQLite3 database

Then write the following queries (also with `sqlite3`) to test:

- Count how many rows you have - it should be 249!
- How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category?
- (*Stretch*) What are the average number of reviews for each category?

Your code (to reproduce all above steps) should be saved in
`buddymove_holidayiq.py`, and added to the repository along with the generated
SQLite database.

## Resources and Stretch Goals

For a more complicated example SQLite database with a number of tables to play
with, check out this [SQLite Sample
Database](https://www.sqlitetutorial.net/sqlite-sample-database/).

The RPG data also exists in a [JSON
file](https://github.com/LambdaSchool/Django-RPG/blob/master/testdata.json) -
try loading it with the standard [json
module](https://docs.python.org/3.5/library/json.html), and reproducing the
above queries with direct manipulation of the Python dictionaries. Also, try to
load it into a `pandas` dataframe and reproduce the above queries with
appropriate dataframe function calls.

This database is part of a Django (Python webapp framework) application, the
[Django-RPG](https://github.com/LambdaSchool/Django-RPG/tree/master) - check it
out, and (though this is very much a stretch goal) you can [get started with
Django](https://www.djangoproject.com/start/) and see if you can run it
(definitely use `pipenv`!). If you are able to, then you can use the the [Django
ORM](https://docs.djangoproject.com/en/2.1/topics/db/) (object-relational
mapping, a way to interact with SQL through programming language objects), and
[query](https://docs.djangoproject.com/en/2.1/topics/db/queries/) the data.
You'll find that the questions we answered with pure SQL are remarkably simple
to answer using the ORM.

If you need one more stretch goal - the RPG data was generated using
[django-autofixture](https://github.com/volrath/django-autofixture), a tool that
facilitates tests by randomly generating data. Check it out, and if you got
Django working, see if you can generate more data.
