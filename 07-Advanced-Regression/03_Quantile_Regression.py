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

# <strong id="tocheading">Table of Contents</strong>
# <div id="toc"></div>

# + {"language": "javascript"}
# $.getScript('https://kmahelona.github.io/ipython_notebook_goodies/ipython_notebook_toc.js')

# + {"colab_type": "text", "id": "SV7gaADiicnV", "cell_type": "markdown"}
# # Quantile Regression
#
# Regressing towards the median - or any quantile - as a way to mitigate outliers and control risk.

# + {"colab_type": "text", "id": "6klMj4q3iqMh", "cell_type": "markdown"}
# ## Lecture
#
# Let's look at data that has a bit of a skew to it:
#
# http://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data

# + {"colab": {}, "colab_type": "code", "id": "yw1AD_z9O0xL"}
import pandas as pd
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/'
                 '00381/PRSA_data_2010.1.1-2014.12.31.csv')

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 206}, "colab_type": "code", "id": "RTlH1lJ8PDv5", "outputId": "e073db49-81bd-4ebd-f43b-69c92aea8467"}
df.head()

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 320}, "colab_type": "code", "id": "m-yC9OSPPFo8", "outputId": "d5602fe7-31ad-458e-d466-212c99e51cf4"}
df.describe()

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 347}, "colab_type": "code", "id": "hfV3WisFP_O6", "outputId": "a9809666-6c33-4778-fe1c-f3030f89d431"}
df['pm2.5'].plot.hist();

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "OgbMTAHzQJB8", "outputId": "15e18384-ede7-4ccd-8961-280b35f66f85"}
# How does linear regression handle it?
from sklearn.linear_model import LinearRegression

# Let's drop NAs and limit to numeric values
df = df._get_numeric_data().dropna()
X = df.drop('pm2.5', axis='columns')
y = df['pm2.5']

linear_reg = LinearRegression().fit(X, y)
linear_reg.score(X, y)

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 462}, "colab_type": "code", "id": "-viFFtm0RizM", "outputId": "256d7680-1a43-4958-c74c-31aaef917906"}
# Not bad - but what if we wanted to model the distribution more conservatively?
# Let's try quantile
import statsmodels.formula.api as smf

# Different jargon/API in StatsModel documentation
# "endogenous" response var is dependent (y), it is "inside"
# "exogenous" variables are independent (X), it is "outside"
# Bonus points - talk about "exogenous shocks" and you're a bona fide economist

# ~ style formulas look like what R uses
# y ~ x1 + x2 + ...
# Also, these formulas break with . in variable name, so lets change that
df = df.rename(index=str, columns={'pm2.5': 'pm25'})

# Now let's construct the formula string using all columns
quant_formula = 'pm25 ~ ' + ' + '.join(df.drop('pm25', axis='columns').columns)
print(quant_formula)

quant_mod = smf.quantreg(quant_formula, data=df)
quant_reg = quant_mod.fit(q=.5)
quant_reg.summary()  # "summary" is another very R-thing

# + {"colab_type": "text", "id": "ZBkP4bewd-HT", "cell_type": "markdown"}
# That fit to the median (q=0.5), also called "Least Absolute Deviation." The pseudo-R^2 isn't really directly comparable to the R^2 from linear regression, but it clearly isn't dramatically improved. Can we make it better?

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 593}, "colab_type": "code", "id": "BgvYeHg3bL4g", "outputId": "bf4547a0-7739-45d8-bf5a-26ab1684f7f6"}
help(quant_mod.fit)

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 1424}, "colab_type": "code", "id": "lpNPioZTei4U", "outputId": "40fc70a6-43c5-44a0-a012-923bd3f826a8"}
quantiles = (.05, .96, .1)

for quantile in quantiles:
  print(quant_mod.fit(q=quantile).summary())

# + {"colab_type": "text", "id": "Xqh4Jp1XgjrE", "cell_type": "markdown"}
# "Strong multicollinearity", eh? In other words - maybe we shouldn't throw every variable in our formula. Let's hand-craft a smaller one, picking the features with the largest magnitude t-statistics for their coefficients. Let's also search for more quantile cutoffs to see what's most effective.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 975}, "colab_type": "code", "id": "NmoELnXwgpXd", "outputId": "1865f1b1-778a-4e73-91b7-d30ad29b2ee2"}
quant_formula = 'pm25 ~ DEWP + TEMP + Ir + hour + Iws'
quant_mod = smf.quantreg(quant_formula, data=df)
for quantile in range(50, 100):
  quantile /= 100
  quant_reg = quant_mod.fit(q=quantile)
  print((quantile, quant_reg.prsquared))

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 444}, "colab_type": "code", "id": "Bz0GmE5kuwQY", "outputId": "d139eca6-fa58-4f4c-a051-18b3e2d7ee13"}
# Okay, this data seems *extremely* skewed
# Let's trying logging
import numpy as np

df['pm25'] = np.log(1 + df['pm25'])
quant_mod = smf.quantreg(quant_formula, data=df)
quant_reg = quant_mod.fit(q=.25)
quant_reg.summary()  # "summary" is another very R-thing

# + {"colab_type": "text", "id": "8kXcxnNBgizX", "cell_type": "markdown"}
# Overall - in this case, quantile regression is not *necessarily* superior to linear regression. But it does give us extra flexibility and another thing to tune - what the center of what we're actually fitting in the dependent variable.
#
# The basic case of `q=0.5` (the median) minimizes the absolute value of residuals, while OLS minimizes the squared value. By selecting `q=0.25`, we're targeting a lower quantile and are effectively saying that we only want to over-estimate at most 25% of the time - we're being *risk averse*.
#
# Depending on the data you're looking at, and the cost of making a false positive versus a false negative, this sort of flexibility can be extremely useful.
#
# Live - let's consider another dataset! Specifically, "SkillCraft" (data on competitive StarCraft players): http://archive.ics.uci.edu/ml/datasets/SkillCraft1+Master+Table+Dataset

# + {"colab": {}, "colab_type": "code", "id": "ofvwSAZUhWDw"}
# TODO Live!
# Hint - we may only care about the *top* quantiles here
# Another hint - there are missing values, but Pandas won't see them right away

# + {"colab_type": "text", "id": "o2BADEQUirXa", "cell_type": "markdown"}
# ## Assignment - birth weight data
#
# Birth weight is a situation where, while the data itself is actually fairly normal and symmetric, our main goal is actually *not* to model mean weight (via OLS), but rather to identify mothers at risk of having children below a certain "at-risk" threshold weight.
#
# Quantile regression gives us just the tool we need. For the data we are using, see: http://people.reed.edu/~jones/141/BirthWgt.html
#
#     bwt: baby's weight in ounces at birth
#     gestation: duration of pregnancy in days
#     parity: parity indicator (first born = 1, later birth = 0)
#     age: mother's age in years
#     height: mother's height in inches
#     weight: mother's weight in pounds (during pregnancy)
#     smoke: indicator for whether mother smokes (1=yes, 0=no) 
#     
# Use this data and `statsmodels` to fit a quantile regression, predicting `bwt` (birth weight) as a function of the other covariates. First, identify an appropriate `q` (quantile) to target a cutoff of 90 ounces - babies above that birth weight are generally healthy/safe, babies below are at-risk.
#
# Then, fit and iterate your model. Be creative! You may want to engineer features. Hint - mother's age likely is not simply linear in its impact, and the other features may interact as well.
#
# At the end, create at least *2* tables and *1* visualization to summarize your best model. Then (in writing) answer the following questions:
#
# - What characteristics of a mother indicate the highest likelihood of an at-risk (low weight) baby?
# - What can expectant mothers be told to help mitigate this risk?
#
# Note that second question is not exactly a data science question - and that's okay! You're not expected to be a medical expert, but it is a good exercise to do a little bit of digging into a particular domain and offer informal but informed opinions.

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 206}, "colab_type": "code", "id": "HUWKv16FjZsY", "outputId": "11f1ecab-4058-4e48-ac0f-cd7cf488a2f7"}
import pandas as pd
bwt_df = pd.read_csv('http://people.reed.edu/~jones/141/Bwt.dat')
bwt_df.head()

# + {"colab": {"base_uri": "https://localhost:8080/", "height": 300}, "colab_type": "code", "id": "dy5FkUZpkJT_", "outputId": "d4f46328-8e25-4fa5-e5b5-6ffad654c65c"}
bwt_df.describe()

# + {"colab": {}, "colab_type": "code", "id": "Ez8qPLojjlFf"}
# TODO - your work here! Also, add text cells for written questions.

# + {"colab_type": "text", "id": "XY9JGAnJisdB", "cell_type": "markdown"}
# ## Resources and stretch goals

# + {"colab_type": "text", "id": "inFWXSpqmND5", "cell_type": "markdown"}
# Resources:
# - [statsmodels QuantReg example](http://www.statsmodels.org/dev/examples/notebooks/generated/quantile_regression.html)
# - [How Shopify used Quantile Regression in modeling risk](https://medium.com/data-shopify/how-shopify-capital-uses-quantile-regression-to-help-merchants-succeed-10ee1b36b17d)
#
# Stretch goals:
# - Find a dataset where you think quantile regression may be appropriate, and try both it and linear regression - compare/contrast their strengths/weaknesses, and write a summary for which you think is better for the situation and why
# - Check out [deep quantile regression](https://www.kdnuggets.com/2018/07/deep-quantile-regression.html), an approach that uses a custom quantile loss function and Keras to train a quantile model
