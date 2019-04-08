# Adding Data Science to a Web Application

You have a basic working web application, and one that pulls real data (Tweets
and their embeddings) - now it's time to add some data science! We're going to
fit a predictive model based on Tweet embeddings, and allow the client to use
the model to make predictions of which user is more likely to tweet given text.

## Learning Objectives

- Run and report simple online analysis of data from the user or an API
- Run a more complicated offline model, and serialize the results for online use

## Before Lecture

You should already have all needed dependencies and accounts, so use any extra
time to refactor your earlier code and check out some of the stretch goals.
Remember, we're building a system to last, not just exploratory notebook code -
this means it's worth a bit of extra time to ensure that our code is *clear* and
clean. Also note - clear and clean code is *not* the same thing as clever code.

## Live Lecture Task

In lecture we will add predictive functionality using
[sklearn.linear_model.LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html),
training on Tweet embeddings from our database for given users. We'll accept
client requests via simple forms, and return the results with a new template. We
will start by exploring the code with a REPL or notebook, and then put as much
as we can in the application.

## Assignment

- Reproduce the lecture tasks (logistic regression fitting, predicting,
  returning) in a REPL/notebook, with different (real) data you select and pull
- Continue incorporating the predictive code in the application - you should be
  able to write fairly pure functions, and then invoke them from Flask routes
- Add a form to let the client select two Twitter Users and enter Tweet text to
  predict which user is more likely to tweet the given text
- Add a form to let the client request new Twitter Users be added, and add their
  Tweets/make them available for predictive modeling as well

## Resources and Stretch Goals

- Make the templates fancier! Add more variables to report, and report them.
- Make your forms nicer and more powerful with
  [WTForms](https://wtforms.readthedocs.io/en/stable/crash_course.html)
- Try to add some visualizations or descriptive language to portray the
  strength/confidence of the prediction
- As with hitting APIs, fitting models can take some time - check out
  [Redis](https://github.com/andymccurdy/redis-py), a key-value store
  specialized in caching (you can sign up for a free cloud Redis instance at
  [Redis Labs](https://redislabs.com), and use
  [birdisle](https://birdisle.readthedocs.io/en/latest/) for local development
  and testing)
- Make the webapp more usable - if you're caching models you can list recently
  run models, and possible link to them
- Try different (better?) models - logistic regression is a great tool, but as
  you know there are many approaches out there
- Fit a multinomial classification model (predict between >2 users) - note this
  may be more of a UX challenge (how should the client specify the users) than a
  data science challenge
