# Advanced Regression
As with hypothesis testing, there is a “zoo” of regression techniques. In this sprint we’ll tour some highlights, and give you valuable tools for solving a variety of real-world problems.

Logistic regression constraints the output (the dependent variable) using the logistic function, mapping the real numbers to the unit interval $(0, 1)$. This makes it suitable for binary classification problems, as well as fitting/predicting probabilities (such as likelihood of clicking something). It’s also the foundation for more sophisticated classification models, capable of distinguishing between more than two classes.

Survival analysis, though morbidly named, is useful for modeling anything that has some duration followed by a (potential) event. Customer retention, time spent on site, system up-time, part failure - all of these can be treated as a survival analysis problem.

Quantile regression is similar to ordinary least squares, but instead of estimating the mean the model estimates quantiles (e.g the median or other percentile cutoffs). This can make it more robust to outliers (as the median is more robust in those cases than the mean), and can give a richer analysis of the distribution of the variable being predicted.

Ridge regression is another enhancement to linear techniques, applying regularization to help solve ill-posed problems (situations where, for OLS $Ax = b$, $x$ either has no solution or multiple solutions). Regularization can also help prevent overfitting, another important consideration.

The above still just scratches the surface of what is out there, but is a good starting point and foundation for your own exploration. With these tools you can solve a variety of real-world problems, and provide meaningful value to anyone looking for insight from a data scientist.

### Logistic Regression
Logistic regression is a workhorse - a model that makes the world (or at least the Internet) go round. And you actually already know nearly all about it - it’s essentially a layer or extension of linear regression techniques. It uses the logistic sigmoid function to restrict the output (dependent variable) to the unit interval $(0, 1)$, allowing us to model binary as well as probabilities and more general (multinomial) classification problems.

**Objectives**
* Student should be able to express and explain the intuition and interpretation of Logistic Regression
* Student should be able to use sklearn.linear_model.LogisticRegression to fit and interpret Logistic Regression models

### Survival Analysis
> “But at the laste, as every thing hath ende” - Geoffrey Chaucer, from the poem Troilus and Criseyde

Survival analysis is the formal study of this truism - things end, but when they end is often a very useful question to ask.

**Objectives**
* Student should be able to express and explain the intuition and interpretation of Survival Analysis techniques
* Student should be able to use the Python package lifelines to fit and interpret Survival models

### Quantile Regression
How does ordinary least squares treat outliers? The same it treats everything - it squares them! But for outliers, squaring dramatically increases their already outsized impact on statistics like the mean.

We know from descriptive statistics that the median is more robust to outliers than the mean. This insight can serve us in predictive statistics as well, and is precisely what quantile regression is about - estimating the median (or other quantile) instead of the mean.

**Objectives**
* Student should be able to express and explain the intuition and interpretation of Quantile Regression
* Student should be able to use the StatsModel Python library to fit and interpret Quantile Regression models

### Ridge Regression
Outliers aren’t the only thing that can give a data scientist headaches - sometimes the underlying linear algebra is not a well-posed problem. In other words, $Ax = b$ doesn’t have a unique solution $x$, and so traditional OLS approaches fail.

Relatedly, overfitting can occur in situations where OLS technically “works”, but the structure of what is being predicted relative to the overall dimensionality of the model is such that the model aligns too tightly with the points, and doesn’t generalize or have predictive value.

One approach to mitigate these problems is regularization - adding information to the model, in order to make it more tractable. In particular, we will consider a common regularized model, ridge regression, which is based on Tikhonov regularization.

**Objectives**
* Student should be able to express and explain the intuition and interpretation of Ridge Regression
* Student should be able to use sklearn.linear_model.Ridge to fit and interpret Ridge Regression models
