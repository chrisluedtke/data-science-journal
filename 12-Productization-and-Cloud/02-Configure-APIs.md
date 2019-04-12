#### Productization Module 2, [Consuming Data from an API](https://github.com/LambdaSchool/DS-Unit-3-Sprint-4-Productization-and-Cloud/blob/master/module2-consuming-data-from-an-api/README.md)
1. Review yesterday
2. Templates & Routes
3. APIs

# 1. Review yesterday

## Created repo

https://github.com/new

- Repository name: TwitOff
- Description: A fun web application for comparing and predicting tweets
- Public
- Add .gitignore: Python
- Add a license: MIT

## Cloned repo

From the command line

`git clone https://github.com/your-github-user-name/TwitOff.git`


## Created virtual environment, installed packages

From the command line, in the `TwitOff/` directory

`pipenv install flask flask-sqlalchemy`


## Activated virtual environment

From the command line, in the `TwitOff/` directory

`pipenv shell` (to activate the virtual environment)

`which flask` (to check, should see `/virtualenvs/TwitOff...`)


## Wrote code

#### `TwitOff/twitoff/__init__.py`
```
"""Entry point for TwitOff Flask application."""
from .app import create_app

APP = create_app()
```

#### TwitOff/twitoff/app.py
```
"""Main application and routing logic for TwitOff."""
from flask import Flask
from .models import DB

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'

    return app
```

#### TwitOff/twitoff/models.py
```
"""SQLAlchemy models for TwitOff."""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users that we pull and analyze tweets for."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
```

## Created / Reset Database

From the command line

`FLASK_APP=twitoff:APP flask shell`

`from twitoff.models import *`

`DB.drop_all()`

`DB.create_all()` 

`quit()`


## Ran Flask

`FLASK_APP=twitoff:APP flask run` ([See documentation](http://flask.pocoo.org/docs/dev/cli/#application-discovery) for Windows instructions)

http://127.0.0.1:5000/ (to see your app)

view-source:http://127.0.0.1:5000/ (to see its source)

https://twitoff.herokuapp.com/ (to compare with the reference app)

Ctrl+C to quit


# 2. Templates & Routes

#### Documentation
- [Flask — Rendering Templates](http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates)
- "[Jinja2](http://jinja.pocoo.org/docs/2.10/) is a modern and designer-friendly templating language for Python ... It is fast, widely used and secure"
- [Flask — Routing](http://flask.pocoo.org/docs/1.0/quickstart/#routing)

## Create template

#### TwitOff/twitoff/templates/base.html

```
<!DOCTYPE html>
<html>
  <head>
    <title>TwitOff - {{ title }}</title>
    <link rel="stylesheet" href="https://unpkg.com/picnic"/>
  </head>
  <body>
    <nav>
      <a href="/" class="brand"><span>TwitOff!</span></a>

      <!-- responsive-->
      <input id="bmenub" type="checkbox" class="show">
      <label for="bmenub" class="burger pseudo button">Menu</label>

      <div class="menu">
        <a href="/update" class="button warning">Update Tweets</a>
        <a href="/reset" class="button error">Reset Database</a>
      </div>
    </nav>
    <article class="flex two" style="padding: 3em 1em;">
      <div>
        <h1>{{ title }}</h1>
      </div>
      <div>
        <h2>Users</h2>
      </div>
    </article>
  </body>
</html>
```

#### TwitOff/twitoff/app.py

```
from flask import Flask, render_template
```

Within the `create_app` factory function

```
    def root():
        return render_template('base.html', title='Home')
```

#### Run Flask

From the command line

`FLASK_APP=twitoff:APP flask run`

Ctrl+C to quit


## Update template

#### TwitOff/twitoff/templates/base.html

```
        <h2>Users</h2>
        {% for user in users %}
        <a href="/user/{{ user.name }}"><span class="stack">{{ user.name }}</span></a>
        {% endfor %}
```

#### TwitOff/twitoff/app.py

```
from .models import DB, User
```

```
    def root():
        return render_template('base.html', title='Home', users=User.query.all())
```

## Add User to DB

From the command line

`FLASK_APP=twitoff:APP flask shell`

`from twitoff.models import *`

`u = User(id=2, name='elonmusk')`

`DB.session.add(u)`

`DB.session.commit()`

`quit()`

### Run Flask

`FLASK_APP=twitoff:APP flask run`

Ctrl+C to quit


## Add route

#### TwitOff/twitoff/app.py

Within the `create_app` factory function

```
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset database!')
```

#### Run Flask

From the command line

`FLASK_APP=twitoff:APP flask run`

Ctrl+C to quit


# 3. APIs

## Install packages

From the command line (in the `TwitOff/` directory, with virtual environment activated)

`pipenv install tweepy basilica python-dotenv`

#### Documentation
- [Tweepy](https://tweepy.readthedocs.io/en/3.7.0/)
- [Basilica](https://basilica-client.readthedocs.io/en/latest/quickstart.html)
- [dotenv](http://flask.pocoo.org/docs/1.0/cli/#environment-variables-from-dotenv)

## Create .env file

#### TwitOff/.env

```
# Environment variables
FLASK_APP=twitoff:APP
FLASK_ENV="development"
DATABASE_URL="sqlite:///db.sqlite3"
TWITTER_CONSUMER_KEY=""
TWITTER_CONSUMER_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_ACCESS_TOKEN_SECRET=""
BASILICA_KEY=""
```

## Get Twitter API keys and Access tokens

[Twitter Developer — Create an app](https://developer.twitter.com/en/apps/create)

- _App name:_ twitoff-yournamehere
- _Application description:_ This app analyzes and compares Twitter users, to predict who would be more likely to send a particular tweet. The app just reads tweets, it doesn't send, retweet, or like tweets.
- _Website URL:_ https://twitoff-yournamehere.herokuapp.com
- _Tell us how this app will be used:_ This app will be used for teaching and learning about developing Python Flask web applications with third-party APIs.

Create

Permissions > Edit > Read-only > Save

Keys and tokens > Access token & access token secret > Create

Copy & paste into your `TwitOff/.env` file

## Get Basilica API key

[Basilica — API Keys](https://www.basilica.ai/api-keys/)

_Create API Key Name:_ twitoff-yournamehere

Create

Copy & paste into your `TwitOff/.env` file


## Update app.py to use environment variables

#### TwitOff/twitoff/app.py

```
from os import getenv
from dotenv import load_dotenv

load_dotenv()
```

Within the `create_app` factory function

```
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['ENV'] = getenv('FLASK_ENV')
    DB.init_app(app)
```

## Create twitter.py to access Twitter & Basilica

#### TwitOff/twitoff/twitter.py

```
"""Retrieve Tweets, embeddings, and persist in the database."""
from os import getenv
from dotenv import load_dotenv
import basilica
import tweepy
from .models import DB, Tweet, User

TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_CONSUMER_KEY'),
                                   getenv('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(getenv('TWITTER_ACCESS_TOKEN'),
                              getenv('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))
```

## Interact with the APIs

From the command line

`exit` (to deactivate the virtual environment)

`pipenv shell` (to reactivate the virtual environment and reload environment variables)

`flask shell`

`from twitoff.twitter import *`

`dir()`

`TWITTER`

`dir(TWITTER)`

`twitter_user = TWITTER.get_user('austen')`

`tweets = twitter_user.timeline()`

`len(tweets)`

`tweets[0].text`

`tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')`

`len(tweets)`

`tweet_text = tweets[0].full_text`

`tweet_text`

`tweets[0].id`

`embedding = BASILICA.embed_sentence(tweet_text, model='twitter')`

`embedding`

## Update the data model

#### TwitOff/twitoff/models.py

```
"""SQLAlchemy models and utility functions for TwitOff."""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users corresponding to Tweets in the Tweet table."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    # Tweet IDs are ordinal ints, so can be used to fetch only more recent
    newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets and their embeddings from Basilica."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))  # Allowing for full + links
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
```

## Get user's tweets and embeddings

From the command line

`flask shell`

`from twitoff.twitter import *`

`twitter_user = TWITTER.get_user('austen')`

`tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')`

`db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)`

`DB.session.add(db_user)`

```
for tweet in tweets:
    embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
    db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300], embedding=embedding)
    db_user.tweets.append(db_tweet)
    DB.session.add(db_tweet)
```

`DB.session.commit()`

`quit()`

#### Run Flask

From the command line

`flask run`

Ctrl+C to quit

# [Assignment](https://github.com/LambdaSchool/DS-Unit-3-Sprint-4-Productization-and-Cloud/blob/master/module2-consuming-data-from-an-api/README.md#assignment)
