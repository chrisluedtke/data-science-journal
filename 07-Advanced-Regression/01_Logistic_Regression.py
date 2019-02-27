# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Logistic Regression

# +
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

pd.options.display.max_columns = None
# -

# **Resources**
# - [5 Reasons “Logistic Regression” should be the first thing you learn when becoming a Data Scientist](https://towardsdatascience.com/5-reasons-logistic-regression-should-be-the-first-thing-you-learn-when-become-a-data-scientist-fcaae46605c4)
# - [Logistic regression from scratch in numpy](https://blog.goodaudience.com/logistic-regression-from-scratch-in-numpy-5841c09e425f) - more code and math, with gradient descent and the logistic loss function
# - more classification models from scikit-learn: [SVM](https://scikit-learn.org/stable/modules/svm.html#classification), [decision trees](https://scikit-learn.org/stable/modules/tree.html#classification), and [naive Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html). The underlying math varies significantly, but the API and interpretation are fairly similar
# - More on [music informatics](https://en.wikipedia.org/wiki/Music_informatics), how audio features were actually calculated in the FMA dataset used at the end of this notebook

# There are many options for regression. Recall that **linear regression** is helpful when predicting a real number along some continuum without a restricted range. Things like income and age.
#
# But what about . . .
# * probabilities
# * binary values (sick vs. healthy, male vs. female)
# * approval rating (0% to 100%)
#
# We need some "squishification" process to map numbers from a real number continuum to the unit interval (X range $-\infty$ to $\infty$, Y range 0 to 1). We need a **cumulative density function** - most commonly the **[sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function)**. This function in particular is useful because its calculous properties give it nice behaviors. (e^x derivative is e^x) Another common CDF is the **[probit function](https://en.wikipedia.org/wiki/Probit)** for probabilities.
#
# With logistic regression, we can even model general multinomial classification problems by combining several logistic regressions to predict membership in various classes and outputting the class that is most likely.
#
# At its heart, logistic regression is still linear. That is, the underlying math and optimization follow traditional linear regression. However, our coefficients won't have intuitive linear interpretation.
#
# $S(x) = \frac{1}{1 + e^{-x}} = \frac{e^x}{e^x + 1}$
#
#
# **What data science methods are used at work?** (source: [Kaggle 2017 Survey](https://www.kaggle.com/surveys/2017))
# ![](img/kaggle-common-algos.PNG)
#
# Logistic regression is the baseline for classification models, as well as a handy way to predict probabilities (since those too live in the unit interval). While relatively simple, it is also the foundation for more sophisticated classification techniques such as neural networks (many of which can effectively be thought of as networks of logistic models).

# ## Example 1: Linear vs. Logistic, Return of the Titanic 🚢
#
# To pull Titanic data from Kaggle:
# * create account
# * generate API Key and `kaggle.json`
# * join [Titanic competition](https://www.kaggle.com/c/titanic/data)
#
# The [Kaggle API](https://github.com/Kaggle/kaggle-api) enables lots of convenient methods for interacting with Kaggle.
#
# Here's how the data were sourced:
# ```python
# # !pip install kaggle
#
# import os, json
#
# path_to_config = "../kaggle.json"
# kaggle_config = json.loads(open(path_to_config).read())
# os.environ['KAGGLE_USERNAME'] = kaggle_config['username']
# os.environ['KAGGLE_KEY'] = kaggle_config['key']
#
# # !kaggle competitions download -c titanic -p datasets/titanic
# ```

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 487}, "colab_type": "code", "id": "-PtztP8YlFym", "outputId": "8b18c64d-988a-44b1-e988-9de3fa61a5d7"}
# How would we try to do this with linear regression?
train_df = pd.read_csv('datasets/titanic/train.csv').dropna()
test_df = pd.read_csv('datasets/titanic/train.csv').dropna()  # Unlabeled, for Kaggle submission

train_df.head()

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "QiZn2p1K8DED", "outputId": "be8b1a4c-ca08-4bba-98ed-3cda0942499c"}
predictors = ['Pclass', 'Age', 'Fare']
target = 'Survived'

X = train_df[predictors]
y = train_df[target]

linear_reg = LinearRegression().fit(X, y)
print('score:', linear_reg.score(X, y))

linear_reg.predict(test_df[predictors])[:10]
# -

# How can you "partially" survive? You either survived or did not, like how our target column is encoded.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "fcxfpsjdFJwM", "outputId": "590a3bba-67fe-48b4-bf6e-91e67bd29bd4"}
{attr: coef for attr, coef in zip(predictors, linear_reg.coef_)}

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "AFiisZU7_2Fr", "outputId": "97e9d9e2-6c2f-49b9-9955-e956b8d42e2a"}
test_case = np.array([[1, 5, 500]])  # Rich 5-year old in first class
linear_reg.predict(test_case)
# -

# How can survial be greater than 1?

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 89}, "colab_type": "code", "id": "dpUm8Dl-u2aB", "outputId": "44bc9b92-52ac-4e13-ab03-e87cbfd5fea7"}
log_reg = LogisticRegression().fit(X, y)
print(log_reg.score(X, y))

log_reg.predict(test_df[predictors])[:10]

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "r7xWwqBrFuWL", "outputId": "4ea8705c-82b5-4378-cd8d-d0aca8e5d19e"}
log_reg.predict(test_case)[0]

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "flF3pcMHGGWw", "outputId": "4d5eef4c-e431-4486-b70f-dde06b7e3862"}
log_reg.predict_proba(test_case)[0]

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "9Bq-54noR1uE", "outputId": "b2650236-5573-4f84-d1a8-ce8bc6d1de17"}
# What's the math?
{attr: coef for attr, coef in zip(predictors, log_reg.coef_[0])}

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "Tj0mNL7_XWNV", "outputId": "effe14e5-839d-4ee0-e38d-fb80eef80ce4"}
log_reg.intercept_


# + {"colab": {}, "colab_type": "code", "id": "AroeYscqR75f"}
# The logistic sigmoid "squishing" function, implemented to accept numpy arrays
def sigmoid(x):
    return 1 / (1 + np.e**(-x))


# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "804BA7s0SggQ", "outputId": "61e0fcc7-adf9-4077-ba27-de875165cea1"}
sigmoid(log_reg.intercept_ + np.dot(log_reg.coef_, np.transpose(test_case)))
# -

# So, clearly a more appropriate model in this situation! For more on the math, [see this Wikipedia example](https://en.wikipedia.org/wiki/Logistic_regression#Probability_of_passing_an_exam_versus_hours_of_study).
#
# **Note:** while the sign (-/+) of coefficients provides information on the relationship between X and Y, we can't infer that a one-unit difference in X corresponds to a one-unit difference in Y.

# ## Example 2: Multinomial Logistic Regression
#
# [Absenteeism at work dataset](http://archive.ics.uci.edu/ml/datasets/Absenteeism+at+work) has 21 classes. `sklearn.linear_model.LogisticRegression` automatically handles more than two classes by essentially treating each label as different (1) from some base class (0).
#
# Here's how the data were sourced:
#

# +
data_url = ('http://archive.ics.uci.edu/ml/'
            'machine-learning-databases/00445/'
            'Absenteeism_at_work_AAA.zip')

extract_zip_url(data_url, 'datasets/abs')
# -

df = pd.read_csv('datasets/abs/Absenteeism_at_work.csv', sep=';')
pd.options.display.max_columns = df.shape[1]
df.head()


def multinom_logistic(df, target, predictors, test_size=0.5, random_state=42):
    X = df[predictors]
    y = df[target]

    if test_size:
        X_train, X_test, Y_train, Y_test = (
            train_test_split(X, y, test_size=test_size, 
                             random_state=random_state)
        )
    else:
        X_train, X_test = [X] * 2
        Y_train, Y_test = [y] * 2
        
    model = LogisticRegression(random_state=random_state, solver='lbfgs', 
                               multi_class='multinomial', max_iter=5000)

    model.fit(X_train, Y_train)
    print('score:', model.score(X_test, Y_test))
    
    return model, X_test, Y_test


target = 'Reason for absence'
predictors = sorted(list(set(df.columns) - 
                         set(['ID', 'Reason for absence'])))

# without train-test
model = multinom_logistic(df, target, predictors, test_size=None, random_state=42)

model = multinom_logistic(df, target, predictors, test_size=0.5, random_state=42)

# smaller test size makes worse score
model = multinom_logistic(df, target, predictors, test_size=0.2, random_state=42)

# + {"colab_type": "text", "id": "iblW74C8afuR", "cell_type": "markdown"}
# ## Example 3: real-world classification
#
# We're going to check out a larger dataset - the [FMA Free Music Archive data](https://github.com/mdeff/fma). It has a selection of CSVs with metadata and calculated audio features that you can load and try to use to classify genre of tracks. To get you started:
# -

# - Clean up the variable names in the dataframe
# - Use logistic regression to fit a model predicting (primary/top) genre
# - Inspect, iterate, and improve your model
# - Answer the following questions (written, ~paragraph each):
#   - What are the best predictors of genre?
#   - What information isn't very useful for predicting genre?
#   - What surprised you the most about your results?

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 454}, "colab_type": "code", "id": "SsySnuKaKtQf", "outputId": "d2855f29-b12c-4c1d-b86e-5867510e797a"}
# # downloads 1.36 GB
# data_url = 'https://os.unil.cloud.switch.ch/fma/fma_metadata.zip'
# extract_zip_url(data_url, 'datasets/fma', flatten=True)

# +
headers = pd.read_csv('datasets/fma/tracks.csv', nrows=3, 
                      header=None)
cols = (headers.T.fillna('')
               .apply(lambda x: ('_'.join(x.astype(str))
                                    .strip('_')), axis=1))

tracks = pd.read_csv('datasets/fma/tracks.csv', skiprows=3, 
                     header=None, names=cols)

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 452}, "colab_type": "code", "id": "_qzn-IjIM1Pw", "outputId": "8b4fd4af-feff-49f0-d2ec-da238c58b716"}
print(tracks.shape)
tracks.head()
# -

target = 'track_genre_top'
target_aliases = ['track_genres', 'track_genres_all']
predictors = ['track_duration', 'track_favorites', 'track_interest', 
              'track_listens', 'artist_latitude', 'artist_longitude']

tracks = tracks.dropna(subset=[target]+predictors)

model, X_test, Y_test = (
    multinom_logistic(tracks, target, predictors,
                      test_size=0.5, random_state=42)
)

# +
from collections import Counter

predictions = model.predict(X_test)

d = {key:0 for key in set(Y_test)}
for actual, predict in zip(Y_test, predictions):
    if actual==predict:
        d[actual] += 1

counts = Counter(Y_test)

for key, value in d.items():
    d[key] = d[key] / counts[key]

prev = pd.Series(counts, name='% prevalence') / len(Y_test) * 100
correct = pd.Series(d, name='% correct') * 100

print(pd.DataFrame([prev, correct]).T.round(1))

# + {"colab_type": "text", "id": "kQUVlUKQMPPW", "cell_type": "markdown"}
# *Important caveats*:
# - This is going to be difficult data to work with - don't let the perfect be the enemy of the good!
# - Be creative in cleaning it up - if the best way you know how to do it is download it locally and edit as a spreadsheet, that's OK!
# - If the data size becomes problematic, consider sampling/subsetting
# - You do not need perfect or complete results - just something plausible that runs, and that supports the reasoning in your written answers
#
# If you find that fitting a model to classify *all* genres isn't very good, it's totally OK to limit to the most frequent genres, or perhaps trying to combine or cluster genres as a preprocessing step. Even then, there will be limits to how good a model can be with just this metadata - if you really want to train an effective genre classifier, you'll have to involve the other data (see stretch goals).
#
# This is real data - there is no "one correct answer", so you can take this in a variety of directions. Just make sure to support your findings, and feel free to share them as well! This is meant to be practice for dealing with other "messy" data, a common task in data science.
