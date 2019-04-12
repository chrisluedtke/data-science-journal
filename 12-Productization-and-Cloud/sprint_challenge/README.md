# Data Science Unit 3 Sprint Challenge 4

## Air Quality in the Cloud

In this sprint challenge you will build a Flask-powered web application that
displays data about air quality. You may use any tools and references you wish,
but your final code should reflect *your* work and be saved in `.py` files
(*not* notebooks), and added to your
`DS-Unit-3-Sprint-4-Productization-and-Cloud` repo, in a new `sprint-challenge`
directory.

You may use any imports/environments/tools you wish, but the baseline is:
- `flask`, `flask-sqlalchemy` to build the application and data models
- `requests` (as a dependency for API access)

If you want to complete all goals (to earn a 3), more dependencies will be
required. Start simple! Only attempt stretch goals if you hit the baseline.

It is also *optional* to manage your environment (e.g. `pipenv`) - it's highly
suggested if available, but `pip install Flask Flask-SQLAlchemy requests` is
adequate for passing.

This file is Markdown, so it may be helpful to add/commit/push it first so you
can view it all nice and rendered on GitHub.

Good luck!

### Part 1 - If I could put Flask in a File

This week we worked on a larger Flask project, but simple applications can fit
entirely in a single file. Following is starting code for a Flask web
application:

```python
"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def root():
    """Base view."""
    return 'TODO - part 2 and beyond!'
```

Ensure you are in a Python environment that at least has `flask`,
`flask-sqlalchemy`, and `requests`. You can make a new isolated environment with
`pipenv install Flask Flask-SQLAlchemy requests`, or just install it in your
current environment with `pip install Flask Flask-SQLAlchemy requests` - both
work, though `pipenv` is suggested if you have it available.

Finally, run the application with: `FLASK_APP=aq_dashboard.py flask run`

You should see something like:
```
 * Serving Flask app "aq_dashboard.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Visit the given URL in your browser to verify that it works.

A few points:
- It is fine to enable debug mode if that is helpful to you
  (`FLASK_ENV='development'`)
- If you prefer, you may use more files/packaging, but only do that if you are
  confident it won't slow you down (simple goals first!)

### Part 2 - Breathe Easy with OpenAQ

Our application is going to be a dashboard that displays air quality data from
the [Open AQ API](https://docs.openaq.org). This API does not require
authorization and can be accessed directly via HTTP requests. There is also a
Python wrapper for the API, [py-openaq](https://github.com/dhhagan/py-openaq),
to facilitate pulling data
([documentation](http://dhhagan.github.io/py-openaq/api.html)).

Your first goal is to verify that you can pull data from OpenAQ with Python -
you may `pip` or `pipenv install py-openaq` if you wish, but do note that it has
a number of dependencies you'll also have to have in your environment (`pandas`,
`seaborn`, `matplotlib`, `requests`). We really only care about that last one -
[requests](https://pypi.org/project/requests/) - as it is what gets the data
over the network (the other dependencies allow the API object to return more
convenient things like dataframes and plots).

So, you have also been provided with a file `openaq.py` that provides a minimal
wrapper, only depending on `requests`. You'll *still* need to `pip` or `pipenv`
install `requests` (if it's not already in your environment), and then place
`openaq.py` in the same `sprint-challenge/` directory and run `python`:

```python
>>> import openaq
>>> api = openaq.OpenAQ()
>>> status, body = api.cities()
>>> status
200
>>> body
{'meta': {'name': 'openaq-api', 'license': 'CC BY 4.0', 'website':...
```

Requests to OpenAQ return a tuple of `status` (of the HTTP response - 200 is OK)
and the body (the response payload, as a Python dict). The body at the top has a
`meta` key for metadata, and a `results` key for the actual data. One of the
more interesting endpoints is
[Measurements](https://docs.openaq.org/#api-Measurements).

```python
>>> # Assuming we have the api object from above
>>> status, body = api.measurements(city='Los Angeles', parameter='pm25')
>>> status
200
>>> body['meta']
{'name': 'openaq-api', 'license': 'CC BY 4.0', 'website':
'https://docs.openaq.org/', 'page': 1, 'limit': 100, 'found': 3069, 'pages': 31}
>>> len(body['results'])
100
>>> body['results'][:2]
[{'location': '21 de mayo', 'parameter': 'pm25', 'date': {'utc':
'2019-03-08T00:00:00.000Z', 'local': '2019-03-07T21:00:00-03:00'}, 'value':
8.13, 'unit': 'µg/m³', 'coordinates': {'latitude': -37.471182288689,
'longitude': -72.36146284977}, 'country': 'CL', 'city': 'Los Angeles'},
{'location': '21 de mayo', 'parameter': 'pm25', 'date': {'utc':
'2019-03-07T23:00:00.000Z', 'local': '2019-03-07T20:00:00-03:00'}, 'value':
8.13, 'unit': 'µg/m³', 'coordinates': {'latitude': -37.471182288689,
'longitude': -72.36146284977}, 'country': 'CL', 'city': 'Los Angeles'}]
```

We are pulling 100 observations of measurements of fine particulate matter (PM
2.5) in the Los Angeles area. Note that this is equivalent to making a request
to this URL (you can even see the data in your browser!):
https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25

Run the above examples (you will get different data - it's a live API!) locally,
and then incorporate the specific request
`api.measurements(city='Los Angeles', parameter='pm25')` into your application:

- Import and set up the API object in your `aq_dashboard.py` file
- Retrieve the data from the API when the main route is called
- Create a list of `(utc_datetime, value)` tuples, e.g. the first two tuples for the
  data returned above would be: `[('2019-03-08T00:00:00.000Z', 8.13),
  ('2019-03-07T23:00:00.000Z', 8.13)]`
- Return this list in the main route, so loading the web application prints the
  raw list of tuples of datetimes and values
  
Getting this list of tuples may be trickier than you think - the API returns
dictionaries inside dictionaries! You may want to use the REPL to experiment and
iterate until you find working code, and then add it to your application.

Hint - Flask routes can return strings, so if you call `str()` on your list of
tuples to convert it, the entire resulting string can be returned.

Another hint - put the logic for pulling a processing results (into the list of
tuples) in a separate function from the `root()` route - the route can just call
it, cast the result to a string, and return that.

*Stretch goal* - read the API documentation and add another interesting request,
and a view that triggers and returns it. But get the rest done before you try
this!

### Part 3 - That Data Belongs In A Model!

As with reservations, *taking* data is great - but *holding* is the most
important part. Let's use `flask-sqlalchemy` to keep our data in a durable
store - a database. Create a `Record` model - you can start by adding the
following code to `aq_dashboard.py`:

```python
from flask_sqlalchemy import SQLAlchemy

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return 'TODO - write a nice representation of Records'


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'
```

This creates a SQLite database with a `Record` table suitable for holding the
list of tuples you created in part 2. Use that logic/list, and add all the
pulled records to the database. As the `Record` class indicates, store the
datetime as a string - SQL does support native `datetime` objects, and as a
stretch goal you can explore and try to implement that.

Also, while the provided `Record` class is adequate for storage, you should
implement the `__repr__` method to provide a nicer representation, so when the
objects are printed or converted to string you can clearly see their time and
values.

To test and verify, you can execute`FLASK_APP=aq_dashboard.py flask shell`:

```
>>> from aq_dashboard import Record
>>> Record.query.all()[:5]
[< Time 2019-03-08T01:00:00.000Z --- Value 9.48 >, < Time
2019-03-08T00:00:00.000Z --- Value 3.0 >, < Time 2019-03-08T00:00:00.000Z ---
Value 8.13 >, < Time 2019-03-07T23:00:00.000Z --- Value 3.0 >, < Time
2019-03-07T23:00:00.000Z --- Value 8.13 >]
```

(Your string format does not need to look exactly as the above, but should
contain comparable information.)

### Part 4 - Dashboard to the Finish

Now that your data is in a database, revisit your main route - instead of
pulling all data live, query the database for any `Record` objects that have
`value` greater or equal to 10. The
[filter](https://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.filter)
method of SQLALchemy queries will be invaluable for this. Hint - your query
should look like `Record.query.filter(condition).all()`, where `condition` is a
comparison/statement that returns a boolean (true/false), and you can access the
fields of `Record` to make that comparison.

Finally, return this filtered list of "potentially risky" PM 2.5 datetime/value
tuples (again, you should make it a string for Flask). You now have a (very
basic) dashboard, that stores, updates, and displays useful data! Note - you may
get few or possibly even no values above the threshold. You can doublecheck by
investigating the raw data, but that may be correct - it just means Los Angeles
happens to have fairly clean air right now!

*Stretch goal* - make it more usable! Put the results in a simple template (for
loop with list items) so they look nicer, and add a link to trigger pulling the
data.

*Super stretch goals* - add a form so the user can specify which city to get a
list of data for. Store data for different types of requests in the database,
and connect the entities appropriately with relations. Instead of dropping all
data for every pull, only add actually new data and keep the rest. Instead of
just listing records that are above a threshold, do some actual data science on
the data (averages, trends, models) and display those results. **Deploy!**

*None of these are realistic to do in a sprint challenge, but if you like this
topic feel free to run with it and make a personal project out of it. Just
please don't share the base solution itself - thanks!*

### Part 5 - Turn it in!
At a minimum, add `aq_dashboard.py` to your weekly repo
(`DS-Unit-3-Sprint-4-Productization-and-Cloud`) in a new `sprint-challenge/`
directory. It is fine to add other files (e.g. `openaq.py`), and if you wrote
any additional files (including a `Pipfile` or `requirements.txt` to facilitate
deployment), include those as well.

Please also add a screenshot of your running application loaded locally in a web
browser, to facilitate grading. Commit, push, and await feedback from your PM.
Thanks for your hard work!

If you got this far, check out the the [official OpenAQ data web
application](https://openaq.org/#/map) - it looks impressive, but really it's
just built on another API ([OpenStreetMap](https://www.openstreetmap.org/)).
Also, read up more on [PM
2.5](https://www.health.ny.gov/environmental/indoors/air/pmq_a.htm) and how it
relates to health.
