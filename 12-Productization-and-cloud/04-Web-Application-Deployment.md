# Web Application Deployment

You have a cool web application going - but it's not really on the *web* yet.
Linking to a GitHub repo is your portfolio is nice, but linking to a live
working application is better as it has a broader audience. Anybody, whether
they are technical or not, can click and enjoy!

## Learning Objectives

- Deploy a basic (single-server) web application to common cloud services
- Securely connect a deployed web application to a relational database back-end

## Before Lecture

Sign up for a free [Heroku](https://www.heroku.com/) account - you shouldn't
need to provide credit card information. Then read their [getting started on
Herkou with
Python](https://devcenter.heroku.com/articles/getting-started-with-python)
guide, and optionally follow along (the example app is Django, but the process
will be similar with Flask).

Also, do your best to get your app in a good working (or at least stable) state,
so you can follow along with deploying in lecture.

## Live Lecture Task

We'll deploy the app! We'll step through all of the following:

- Creating the app on Heroku
- Adding Heroku as a git remote (Heroku deploys using git)
- Making sure we have an appropriate `Procfile` (tells Heroku the process to
  run)
- Setting config vars (the Heroku equivalent of environment variables)
- Launching and connecting to a Heroku PostgreSQL instance

## Assignment

- Deploy your app! Suggested app name `twitoff-yourusername`
- Debug! You'll definitely have to debug some...
  - `heroku log` is your (command line) friend, as is `heroku run` (see below)
  - Logging into the Heroku control panel in your browser can also help
  - `heroku config:set variable=value` lets you set environment variables
  - `heroku addons:create heroku-postgresql:hobby-dev` creates a free hosted
    PostgreSQL database and assigns the `DATABASE_URL` environment variable
    appropriately ([more
    info](https://devcenter.heroku.com/articles/heroku-postgresql))
- Help your classmates! Deploying is always rough at first, and you'll see and
  learn new things by helping each other as well

## Resources and Stretch Goals

- If you really run into issues with Heroku, you can check out
  [ngrok](https://ngrok.com/) as a way to set up a tunnel that lets you run the
  server locally but serve it to the world - but it isn't really a replacement
  for cloud deployment, as it's only up when you're running it on your computer
- `heroku run` is super powerful - you can use it to run code on your hosted
  application, including `heroku run /bin/bash` to start a shell
- Push the app! See if you can break it, and if you do, if you can fix it
- Try to see how the app scales - free Heroku service will have some limitations
- Incorporate [Redis](https://redislabs.com/) as a cache to mitigate performance
  issues
- An alternative to Heroku for hosting Flask is
  [PythonAnywhere](https://www.pythonanywhere.com/)
  - In some ways it is simpler, and it can even persist a SQLite database file
  - But, it doesn't provide PostgreSQL (you can use
    [ElephantSQL](https://www.elephantsql.com/) instead) and is less widely used
  - Overall: stick with Heroku first, but check out PythonAnywhere if you'd like
- Another alternative (in the other direction) is [AWS](https://aws.amazon.com/)
  - Heroku is nice for prototyping and fairly standard applications (it
    abstracts away a lot of the details, so as long as you fit their use case it
    "just works")
  - But larger more complicated services are often deployed via more powerful
    services like AWS, Google Cloud, and Microsoft Azure
  - Again: Heroku first, and then explore alternatives
- Add some basic permissions or possibly even an account system, so not everyone
  can just add users, pull Tweets, or reset data
