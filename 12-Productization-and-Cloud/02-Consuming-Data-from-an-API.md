# Consuming Data from an API

A data-backed application is only as good as the data it has - and a great way
to get a lot of data is through an API. The idea of an API is actually very
general, but in the modern day usually refers to "asking some other service to
give you (some of) their data." A lot of apps are built this way, especially
when starting out, but there are some steps and hoops to get it working.

## Learning Objectives

- Connect to the Twitter API and query for tweets by various parameters
- Connect to Basilica API and retrieve and manipulate embeddings for given
  entities

## Before Lecture

Sign up for [Twitter Developer
access](https://developer.twitter.com/en/apply-for-access) - this requires
answering various questions about what you will use the API for. Answer
honestly, mentioning that you are a student and will be developing an
application that analyzes the textual content of Tweets for comparing different
Twitter users. Also check out [Tweepy](https://tweepy.readthedocs.io/), a Python
package that facilitates accessing the Twitter API.

Sign up for [Basilica](https://www.basilica.ai), and read and follow their
[Python quickstart](https://www.basilica.ai/quickstart/python/). This service
will let you get embeddings (rich high-dimensional representations of the
"meaning" of a given entity,  e.g. Tweets) to fit predictive models such as
regression. They make their own Python package (`basilica`) for facilitating
access to the API.

## Live Lecture Task

We'll get set up to access both the Twitter and Basilica APIs in our Flask
application, using environment variables (facilitated with [Python
Decouple](https://github.com/henriquebastos/python-decouple)) to ensure we don't
check any secrets into git.

## Assignment

Reproduce the steps from lecture (ensure you can access both the Twitter and
Basilica APIs via Python), then:

- Write methods to pull actual Users and Tweets and replace your invented data
  with actual Twitter data
- Add an `embedding` field to your `Tweet` model, and functions to populate it
  with embeddings returned from Basilica
- Add a `/user/<name>` route and template that pulls and displays user Tweets

## Resources and Stretch Goals

- [Flask routing](http://flask.pocoo.org/docs/1.0/quickstart/#routing) is simple
  but powerful - take advantage of it!
- [https://www.getpostman.com/](Postman) is an app to let you test both your
  routes and a REST API
- Go deeper with the Twitter API - use paging (offset by oldest fetched Tweet
  ID) to pull older Tweets, so you can build a larger set of embedding data for
  a given user
- [twitter-scraper](https://github.com/kennethreitz/twitter-scraper) is another
  approach to getting data from Twitter - no auth required (but Twitter may
  choose to try to break it)
- Make the home page a bit more useful - links to pulled users, descriptive
  text, etc.
- Make your app look nicer - the earlier mentioned [Picnic
  CSS](https://picnicss.com) is an easy way, and
  [Bootstrap](https://getbootstrap.com) is very widely used
- You may notice that pulling lots of Tweets and getting lots of embeddings
  takes a long time (and may even be rate limited) - organize your code in
  functions so these tasks can be performed "offline" (without loading the full
  Flask application)
- Try using some of the other embeddings Basilica can return (images, general
  text) - you can just experiment with it, or see if you can figure out a way to
  incorporate it into the application (e.g. Tweeted photos, etc.)
