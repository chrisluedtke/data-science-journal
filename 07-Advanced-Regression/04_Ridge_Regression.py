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

# + {"colab_type": "text", "id": "-eFju4_DDKeX", "cell_type": "markdown"}
# # Ridge Regression
#
# Regularize your way to a better tomorrow.

# +
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge # NEW!
from sklearn.linear_model import RidgeCV # NEW!
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale # NEW!

plt.style.use('seaborn')
# -

# **Resources**
# - [What is regularization in machine learning](https://www.quora.com/What-is-regularization-in-machine-learning) - quora
# - [how to use regularization to prevent model overfitting](https://blogs.sas.com/content/subconsciousmusings/2017/07/06/how-to-use-regularization-to-prevent-model-overfitting/) - The SAS Data Science Blog
# - [introduction to regularization to reduce overfitting and improve generalization error](https://machinelearningmastery.com/introduction-to-regularization-to-reduce-overfitting-and-improve-generalization-error/) - machinelearningmastery
# - [ridge and lasso regression a complete guide with-python scikit-learn](https://towardsdatascience.com/ridge-and-lasso-regression-a-complete-guide-with-python-scikit-learn-e20e34bcbf0b) - towardsdatascience
# - [Question about Standardizing in Ridge Regression](https://stats.stackexchange.com/questions/111017/question-about-standardizing-in-ridge-regression#111022) - stackexchange

# + {"colab_type": "text", "id": "5v5cBm19JxOj", "cell_type": "markdown"}
# ## Well-Posed Problems
#
# Data science depends on math, and math is generally focused on situations where:
#
# 1. a solution exists,
# 2. the solution is unique,
# 3. the solution's behavior changes continuously with the initial conditions.
#
# These are known as [well-posed problems](https://en.wikipedia.org/wiki/Well-posed_problem), and are the sorts of assumptions so core in traditional techniques that it is easy to forget about them. But they do matter, as there can be exceptions:
#
# 1. no solution - e.g. no $x$ such that $Ax = b$
# 2. multiple solutions - e.g. several $x_1, x_2, ...$ such that $Ax = b$
# 3. "chaotic" systems - situations where small changes in initial conditions interact and reverberate in essentially unpredictable ways - for instance, the difficulty in longterm predictions of weather (N.B. not the same thing as longterm predictions of *climate*) - you can think of this as models that fail to generalize well, because they overfit on the training data (the initial conditions)
#
# Problems suffering from the above are called ill-posed problems. Relating to linear algebra and systems of equations, the only truly well-posed problems are those with a single unique solution.
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/c/c0/Intersecting_Lines.svg" width=200>
#
# Think for a moment - what would the above plot look like if there was no solution? If there were multiple solutions? And how would that generalize to higher dimensions?
#
# A lot of what we covered with linear regression was about getting matrices into the right shape for them to be solvable in this sense. But some matrices just won't submit to this, and other problems may technically "fit" linear regression but still be violating the above assumptions in subtle ways.
#
# [Overfitting](https://en.wikipedia.org/wiki/Overfitting) is in some ways a special case of this - an overfit model uses more features/parameters than is "justified" by the data (essentially by the *dimensionality* of the data, as measured by $n$ the number of observations). As the number of features approaches the number of observations, linear regression still "works", but it starts giving fairly perverse results. In particular, it results in a model that fails to *generalize* - and so the core goal of prediction and explanatory power is undermined.
#
# How is this related to well and ill-posed problems? It's not clearly a no solution or multiple solution case, but it does fall in the third category - overfitting results in fitting to the "noise" in the data, which means the particulars of one random sample or another (different initial conditions) will result in dramatically different models.

# + {"colab_type": "text", "id": "HeWRlRQVe6xm", "cell_type": "markdown"}
# **Two Equations with Two Unknowns (well-posed)**

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 118}, "colab_type": "code", "id": "EwmhM_qJcPju", "outputId": "2d9ff42e-7873-46f8-88e4-89ec9a0cff3e"}
#  x - y = -1
# 3x + y =  9

A = np.array([[1, -1], 
              [3,  1]])
b = np.array([[-1],
              [ 9]])

solution = np.linalg.solve(A, b)
print(solution)
print("x:", solution[0][0])
print("y:", solution[1][0])

# + {"colab_type": "text", "id": "yfCiMDdYdJaF", "cell_type": "markdown"}
# **Two Equations with Three Unknowns (not well-posed)**

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 448}, "colab_type": "code", "id": "X_gt9UZ6dbPn", "outputId": "cdaabf40-39eb-4e65-c2a9-09232bee2342"}
#  x - y +  z = -1
# 3x + y - 2z =  9

A = np.array([[ 1, -1,  1], 
              [ 3,  1, -2]])
b = np.array([[-1],
              [ 9]])

try:
    print(np.linalg.solve(A, b))
except np.linalg.LinAlgError as e:
    print('LinAlgError:', e)

# + {"colab_type": "text", "id": "oJjbQ6SqesXE", "cell_type": "markdown"}
# You can reduce these formulas, but there is no single solution, there are infinitely many solutions where the solution to at least one of these variables must be a function of the other variables.
#
# Example: [Solving a System of 2 Equations with 3 Unknowns - Infinitely Many Solutions - YouTube](https://www.youtube.com/watch?v=tGPSEXVYw_o)

# + {"colab_type": "text", "id": "B4aMQTidku3F", "cell_type": "markdown"}
# # Generalization in Machine Learning
#
# The goal of machine learning is to end up with a model that can predict well on new data that it has never seen before. This is sometimes called "out of sample accuracy". This is what we are simulating when we do a train-test-split. We fit our model to the training dataset and then test its ability to generalize by evaluating its accuracy on a test dataset. We want models that will be usable on new data indefinitely. We can train them once and reap the rewards of accurate predictions for a long time to come. 
#
# ### Underfitting
# An underfit model will not perform well on the test data and will also not generalize to new data. Because of this, we can usually detect it easily (it just performs poorly in all situations - be it train or test). Because it's easy to identify we either remedy it quickly or move onto new methods. 

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 347}, "colab_type": "code", "id": "tnRwvUN-lPeZ", "outputId": "f1bac215-43bf-4a86-9c96-b9578c1f63e5"}
X = np.array(list(range(1,21)))
y = np.array(list(range(10, 0,-1)) + 
             list(range( 1,11, 1)))

plt.scatter(X,y)
plt.show()

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 414}, "colab_type": "code", "id": "eV3fdqYbmQAm", "outputId": "c1902ea1-0101-4b28-8b36-0a72ce21c0e9"}
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.5, random_state=42)

X_train = X_train.reshape(-1, 1)

model = LinearRegression().fit(X_train, y_train)

score = model.score(X_train, y_train)
beta_0 = model.intercept_
beta_1 = model.coef_[0]

print("Score:", score)
print("Slope:", beta_1)
print("Intrc:", beta_0)
print('Train')
plt.scatter(X_train, y_train)
plt.plot([beta_1*x + beta_0 for x in range(25)])
plt.xlim(2, 21); plt.ylim(1, 10)
plt.show()
print('Test')
plt.scatter(X_test, y_test)
plt.plot([beta_1*x + beta_0 for x in range(25)])
plt.xlim(2, 21); plt.ylim(1, 10)
plt.show()

# + {"colab_type": "text", "id": "jtbVuLfCka7n", "cell_type": "markdown"}
# ### Overfitting
#
# Lets explore the problem of overfitting (and possible remedy - Ridge Regression) in the context of some housing data.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 215}, "colab_type": "code", "id": "TDh_Oz9HDHeR", "outputId": "c2f10a7f-27b1-4d8f-fb55-d2aba2488fed"}
from sklearn.datasets import load_boston

boston = load_boston()
boston.data = scale(boston.data)  # Very helpful for regularization!

df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['Price'] = boston.target
df.head()

# + {"colab_type": "text", "id": "KKQeT4-HhIZz", "cell_type": "markdown"}
# **`preprocessing.scale(x)` does the same thing as `preprocessing.StandardScaler()`**
#
# * `.scale(x)` is a function (lowercase naming convention)
# * `StandardScaler()` is a class (uppercase naming convention) with some extra functionality
# * they will both scale our data equally well. 

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "3u24Yr-SkIhb", "outputId": "17c60be8-b4c9-4cfc-e9f0-3f428b0921ec"}
df.shape

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "0vlZShpFkll2", "outputId": "0e6d62d9-8ce7-49f1-fdb9-877068ea1c2d"}
# ordinary least squares regression
X = df.drop('Price', axis='columns')
y = df.Price

lin_reg = LinearRegression().fit(X, y)
lin_reg_mse = mean_squared_error(y, lin_reg.predict(X))
print('lin_reg_mse:', lin_reg_mse)

# + {"colab_type": "text", "id": "erOFuJKWlTad", "cell_type": "markdown"}
# That seems like a pretty good score, but **chances are this doesn't generalize very well**.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 50}, "colab_type": "code", "id": "CG6DZ1UcqbEx", "outputId": "72249417-706c-40f0-d5e3-631119439692"}
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=43)

lin_reg_split = LinearRegression().fit(X_train, y_train)
lin_reg_train_mse = mean_squared_error(y_train, lin_reg_split.predict(X_train))
lin_reg_test_mse = mean_squared_error(y_test, lin_reg_split.predict(X_test))
print('lin_reg_train_mse:', lin_reg_train_mse)
print('lin_reg_test_mse:', lin_reg_test_mse)

# + {"colab_type": "text", "id": "ILHGe53Iqehg", "cell_type": "markdown"}
# When split into train and test, we see evidence of overfitting. We fitting well to training data, but did not generalize well to test data. What can we do?
#
# - **Use fewer features.** But it can be a lot of work to figure out *which* features, and (in cases like this) there may not be any good reason to really favor some features over another.
# - **Get more data.** This is actually a pretty good approach in tech, since apps generate lots of data all the time (and we made this situation by artificially constraining our data). But for case studies, existing data, etc. it won't work.
# - **Regularize!**

# + {"colab_type": "text", "id": "ILHGe53Iqehg", "cell_type": "markdown"}
# # Regularization
#
# **Intuition:** Regularization just means "add bias". There's more to it than that, but that's the core intuition.
#
# Our model is working "too well", so we fix it by making it harder for the model! A technique that is purposefully "worse" can actually get better results.
#
# In the context of statistics and machine learning, **bias** is when a predictive model fails to identify relationships between features and the output. In a word, bias is *underfitting*.
#
# We want to add bias to the model because of the [bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) - variance is the sensitivity of a model to the random noise in its training data (i.e. *overfitting*), and bias and variance are naturally (inversely) related. Increasing one will always decrease the other, with regards to the overall generalization error (predictive accuracy on unseen data).
#
# Visually, the result looks like this:
#
# <img src="https://upload.wikimedia.org/wikipedia/commons/0/02/Regularization.svg" width=200>
#
# * Both lines are "overfit" - they both include all data points.
# * The **blue line** uses more extreme coefficients than are needed (we assume both lines have the same polynomial terms). We can intuit that much of the movement is based on noise and it won't generalize well.
# * The **green line** is less susceptible to the noise - depending on how exactly we parameterize "noise" we may throw out actual correlation, but if we balance it right we keep that signal and greatly improve generalizability.
# -

# ## Regularization via ridge regression in `sklearn`

print('lin_reg_mse      :', lin_reg_mse)
print('lin_reg_train_mse:', lin_reg_train_mse)
print('lin_reg_test_mse :', lin_reg_test_mse)

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "7aQlX9e9lQLr", "outputId": "8d9ac11c-6ba9-4056-bf8e-6a4f6c6eef3f"}
# Now with regularization via ridge regression
ridge_reg = Ridge().fit(X, y)
ridge_reg_mse = mean_squared_error(y, ridge_reg.predict(X))
print(ridge_reg_mse)
# -

# Without train-test split, the score is a bit worse than OLS - but that's expected since we've added bias.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "qiMXYAWGomcB", "outputId": "9c650108-e1c2-4651-9f78-005bd9d23b24"}
ridge_reg_split = Ridge().fit(X_train, y_train)
print('ridge_reg_train_mse:', mean_squared_error(y_train, ridge_reg_split.predict(X_train)))
print('ridge_reg_test_mse :', mean_squared_error(y_test, ridge_reg_split.predict(X_test)))
# -

# A little better! Can we improve it further? We used default arguments to `Ridge()`, but as always there are plenty of parameters.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 4522}, "colab_type": "code", "id": "PJhjFFeF2uoA", "outputId": "803900e0-051a-4391-b177-4e0eee896f1e"}
help(Ridge)

# + {"colab_type": "text", "id": "F4eY9TKw4S4F", "cell_type": "markdown"}
# How to tune alpha? For now, let's loop and try values. (For longterm/stretch/next week, check out [cross-validation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeCV.html#sklearn.linear_model.RidgeCV).)

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 3574}, "colab_type": "code", "id": "DISx148Z4Sqi", "outputId": "cf20b3dd-9827-4fc4-b0c0-6b4948ef604c"}
mses = {}
for a in range(0, 150, 1):
    ridge_reg_split = Ridge(alpha=a).fit(X_train, y_train)
    mses[a] = mean_squared_error(y_test, ridge_reg_split.predict(X_test))

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 347}, "colab_type": "code", "id": "iRB3KHyWiO4y", "outputId": "fc962a0c-c9ca-48c6-c491-a25f57cec656"}
plt.scatter(mses.keys(), mses.values());

# + {"colab_type": "text", "id": "WzgTBd-FcctM", "cell_type": "markdown"}
# ## The Inuition
#
# The `alpha` parameter corresponds to the weight being given to the extra penalty being calculated by [Tikhonov regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization) (this parameter is sometimes referred to as $\lambda$ in the context of ridge regression).
#
# Normal linear regression (OLS) minimizes the **sum of square error of the residuals**.
#
# Ridge regression minimizes the **sum of square error of the residuals** *AND* **the squared slope of the fit model, times the alpha parameter**.
#
# Therfore a Ridge model with `alpha=0` is the same as that found via linear regression!
#
# As `alpha` is increased, we give more and more penalty to a steep slope. In two or three dimensions this is fairly easy to visualize - beyond, think of it as penalizing coefficient size. Each coefficient represents the slope of an individual dimension (feature) of the model, so ridge regression is just squaring and summing those.
#
# So while `alpha=0` reduces to OLS, as `alpha` approaches infinity eventually the penalty gets so extreme that the model will always output every coefficient as 0 (any non-zero coefficient resulting in a penalty that outweighs whatever improvement in the residuals), and just fit a flat model with intercept at the mean of the dependent variable.
#
# Of course, what we want is somewhere in-between these extremes. Intuitively, we want to apply an appropriate cost/penalty to the model for fitting parameters, much like adjusted $R^2$ takes into account the cost of adding complexity to a model. The "appropriate" penalty will vary.
#
# **Note:** scaling the data helps. Then our cost is consistent and can be added uniformly across features, and it is simpler to search for the `alpha` parameter.
#
# ### Bonus - magic! ✨
#
# Ridge regression doesn't just reduce overfitting and help with the third aspect of well-posed problems (poor generalizability). It can also fix the first two (no unique solution)!

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 50}, "colab_type": "code", "id": "rdogs9EMX6Vd", "outputId": "d5cf4ca9-8dba-4031-b106-fcae6015cd97"}
df_tiny = df.sample(10, random_state=27)
print(df_tiny.shape)
X = df_tiny.drop('Price', axis='columns')
y = df_tiny.Price

lin_reg = LinearRegression().fit(X, y)
print(lin_reg.score(X, y))
# -

# Perfect multi-collinearity! True OLS would 💥 here. `sklearn` protects us from actual error, but still gives a poor model

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "zesVR59NhA7A", "outputId": "fed3b781-60fa-4810-f898-aa3567e6eaad"}
ridge_reg = Ridge().fit(X, y)
ridge_reg.score(X, y)  # More plausible (not "perfect")

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "WP6zwLtshaVR", "outputId": "382c851e-1c73-4413-a73d-e58d6cffa4a5"}
# Using our earlier test split
mean_squared_error(y_test, lin_reg.predict(X_test))

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "QeL_O8vNhSqj", "outputId": "07edce43-61e2-4edf-8094-bd522cb3c647"}
# Ridge generalizes *way* better, even wihtout tuning our alpha
mean_squared_error(y_test, ridge_reg.predict(X_test))

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "WetquM-DVgu5", "outputId": "3237aa3f-acbb-404e-b69c-ac4134b83aa3"}
# from sklearn.linear_model import RidgeCV
ridgecv = RidgeCV(alphas=list(range(0,20))).fit(X, y)
ridgecv.score(X, y)
print('Best alpha:', ridgecv.alpha_)
print(mean_squared_error(y_test, ridgecv.predict(X_test)))

# + {"colab_type": "text", "id": "x2N5WDV6nd3S", "cell_type": "markdown"}
# ## And a bit more math
#
# The regularization used by Ridge Regression is also known as **$L^2$ regularization**, due to the squaring of the slopes being summed. This corresponds to [$L^2$ space](https://en.wikipedia.org/wiki/Square-integrable_function), a metric space of square-integrable functions that generally measure what we intuitively think of as "distance" (at least, on a plane) - what is referred to as Euclidean distance.
#
# The other famous norm is $L^1$, also known as [taxicab geometry](https://en.wikipedia.org/wiki/Taxicab_geometry), because it follows the "grid" to measure distance like a car driving around city blocks (rather than going directly like $L^2$). When referred to as a distance this is called "Manhattan distance", and can be used for regularization (see [LASSO](https://en.wikipedia.org/wiki/Lasso_(statistics%29), which [uses the $L^1$ norm](https://www.quora.com/What-is-the-difference-between-L1-and-L2-regularization-How-does-it-solve-the-problem-of-overfitting-Which-regularizer-to-use-and-when)).
#
# All this comes down to - regularization means increasing model bias by "watering down" coefficients with a penalty typically based on some sort of distance metric, and thus reducing variance (overfitting the model to the noise in the data). It gives us another lever to try and another tool for our toolchest!
#
# # Example 2: Putting it all together
#
# The official scikit-learn documentation has many excellent examples - [this one](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols_ridge_variance.html#sphx-glr-auto-examples-linear-model-plot-ols-ridge-variance-py) illustrates how ridge regression effectively reduces the variance, again by increasing the bias, penalizing coefficients to reduce the effectiveness of features (but also the impact of noise).
#
# ```
# Due to the few points in each dimension and the straight line that linear regression uses to follow these points as well as it can, noise on the observations will cause great variance as shown in the first plot. Every line’s slope can vary quite a bit for each prediction due to the noise induced in the observations.
#
# Ridge regression is basically minimizing a penalised version of the least-squared function. The penalising shrinks the value of the regression coefficients. Despite the few data points in each dimension, the slope of the prediction is much more stable and the variance in the line itself is greatly reduced, in comparison to that of the standard linear regression
# ```

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 425}, "colab_type": "code", "id": "LaOYdswIB6Bo", "outputId": "684be10d-7fbb-40d2-815b-f1ecf10ec877"}
# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

X_train = np.c_[.5, 1].T
y_train = [.5, 1]
X_test = np.c_[0, 2].T

np.random.seed(0)

classifiers = dict(ols=LinearRegression(),
                   ridge=Ridge(alpha=.1))

for name, clf in classifiers.items():
    fig, ax = plt.subplots(figsize=(4, 3))

    for _ in range(6):
        this_X = .1 * np.random.normal(size=(2, 1)) + X_train
        clf.fit(this_X, y_train)

        ax.plot(X_test, clf.predict(X_test), color='gray')
        ax.scatter(this_X, y_train, s=3, c='gray', marker='o', zorder=10)

    clf.fit(X_train, y_train)
    ax.plot(X_test, clf.predict(X_test), linewidth=2, color='blue')
    ax.scatter(X_train, y_train, s=30, c='red', marker='+', zorder=10)

    ax.set_title(name)
    ax.set_xlim(0, 2)
    ax.set_ylim((0, 1.6))
    ax.set_xlabel('X')
    ax.set_ylabel('y')

    fig.tight_layout()

plt.show()

# + {"colab_type": "text", "id": "g7brAGOnx81n", "cell_type": "markdown"}
# Between the first and the second graph, we have decreased the slope (penalized or watered-down coefficients), but we have less variance between our lines)

# + {"colab_type": "text", "id": "k0AhsAmuJzT9", "cell_type": "markdown"}
# # Example 3
#
# Following is data describing characteristics of blog posts, with a target feature of how many comments will be posted in the following 24 hours.
#
# https://archive.ics.uci.edu/ml/datasets/BlogFeedback
#
# ```
# Attribute Information:
#
# 1...50: Average, standard deviation, min, max and median of the Attributes
# 51...60 for the source of the current blog post 
# With source we mean the blog on which the post appeared. 
# For example, myblog.blog.org would be the source of 
# the post myblog.blog.org/post_2010_09_10 
# 51: Total number of comments before basetime 
# 52: Number of comments in the last 24 hours before the 
# basetime 
# 53: Let T1 denote the datetime 48 hours before basetime, 
# Let T2 denote the datetime 24 hours before basetime. 
# This attribute is the number of comments in the time period 
# between T1 and T2 
# 54: Number of comments in the first 24 hours after the 
# publication of the blog post, but before basetime 
# 55: The difference of Attribute 52 and Attribute 53 
# 56...60: 
# The same features as the attributes 51...55, but 
# features 56...60 refer to the number of links (trackbacks), 
# while features 51...55 refer to the number of comments. 
# 61: The length of time between the publication of the blog post 
# and basetime 
# 62: The length of the blog post 
# 63...262: 
# The 200 bag of words features for 200 frequent words of the 
# text of the blog post 
# 263...269: binary indicator features (0 or 1) for the weekday 
# (Monday...Sunday) of the basetime 
# 270...276: binary indicator features (0 or 1) for the weekday 
# (Monday...Sunday) of the date of publication of the blog 
# post 
# 277: Number of parent pages: we consider a blog post P as a 
# parent of blog post B, if B is a reply (trackback) to 
# blog post P. 
# 278...280: 
# Minimum, maximum, average number of comments that the 
# parents received 
# 281: The target: the number of comments in the next 24 hours 
# (relative to basetime)
# ```
#
# Investigate - you can try both linear and ridge. You can also sample to smaller data size and see if that makes ridge more important. Don't forget to scale!
#
# Focus on the training data, but if you want to load and compare to any of the test data files you can also do that.
#
# Note - Ridge may not be that fundamentally superior in this case. That's OK! It's still good to practice both, and see if you can find parameters or sample sizes where ridge does generalize and perform better.
#
# When you've fit models to your satisfaction, answer the following question:
#
# ```
# Did you find cases where Ridge performed better? If so, describe (alpha parameter, sample size, any other relevant info/processing). If not, what do you think that tells you about the data?
# ```
#
# You can create whatever plots, tables, or other results support your argument. In this case, your target audience is a fellow data scientist, *not* a layperson, so feel free to dig in!

# + {"colab": {}, "colab_type": "code", "id": "HKKnNsttRpwI"}
# install and import personal library, extract data zip file from url
# # !pip install --upgrade git+https://github.com/chrisluedtke/clued.git
# from clued.get_data import extract_zip_url, get_uci_data_urls

# uci_url = 'https://archive.ics.uci.edu/ml/datasets/BlogFeedback'
# data_url = get_uci_data_urls(uci_url)
# extract_zip_url(data_url[0], write_path='datasets/blogfeedback')
# -

pd.options.display.max_columns = None
df = pd.read_csv('datasets/blogfeedback/blogData_train.csv', header=None)

print(df.shape)

# +
# 51: n_comments_cum_before
# 52: n_comments_24h_before
# 53: n_comments_24h72h_before
# 54: n_comments_24h_after_post
# 55: The difference of Attribute 52 and Attribute 53 
# 56...60

# +
X = df.iloc[:, 0:280].values
X = scale(X)
y = df.iloc[:,   280].values

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.33, random_state=42)
# -

mses = {}
for a in range(350, 450, 10):
    model = Ridge(alpha=a).fit(X_train, y_train)
    mses[a] = mean_squared_error(y_test, model.predict(X_test))

mses
# alpah ~ 400

model = Ridge(alpha=400).fit(X_train, y_train)
print(mean_squared_error(y_train, model.predict(X_train)))
print(mean_squared_error(y_test, model.predict(X_test)))

# Still overfit!

# + {"colab_type": "text", "id": "o_ZIP6O0J435", "cell_type": "markdown"}
# **Stretch goals**
# - Revisit past data you've fit OLS models to, and see if there's an `alpha` such that ridge regression results in a model with lower MSE on a train/test split
# - Yes, Ridge can be applied to classification! Check out [sklearn.linear_model.RidgeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.RidgeClassifier.html#sklearn.linear_model.RidgeClassifier), and try it on a problem you previous approached with a different classifier (note - scikit LogisticRegression also automatically penalizes based on the $L^2$ norm, so the difference won't be as dramatic)
# - Implement your own function to calculate the full cost that ridge regression is optimizing (the sum of squared residuals + `alpha` times the sum of squared coefficients) - this alone won't fit a model, but you can use it to verify cost of trained models and that the coefficients from the equivalent OLS (without regularization) may have a higher cost
