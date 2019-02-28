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

# # Survival Analysis

# +
# # !pip install lifelines

import lifelines
import numpy as np
import matplotlib.pyplot as plt # version > 3.0
import pandas as pd

plt.style.use('seaborn')
# -

# **Contents**
# * [Overview](#Overview)
#     * Censorship in Data
#     * Hazard Function - the dangerous bathtub
#     * Survival Function (aka reliability function)
#     * Ways to estimate/model survival analysis - terms to be aware of
#     * `lifelines` package
# * [Example 1: Leukemia](#Example-1:-Leukemia)
#     * Kaplan-Meier survival estimate
#     * Cox Proportional Hazards Model -- Survival Regression
# * [Example 2: Recidivism](#Example-2:-Recidivism)
# * [Example 3: Heart Attack Survival](#Example-3:-Heart-Attack-Survival])
# * [Example 4: Customer Churn](#Example-4:-Customer-Churn)
#
# **Resources**
# - [Wikipedia on Survival analysis](https://en.wikipedia.org/wiki/Survival_analysis)
# - [Wikipedia on Survival functions](https://en.wikipedia.org/wiki/Survival_function)
# - [Summary of survival analysis by a biostatistician](http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Survival/BS704_Survival_print.html)
# - [Another medical statistics article on survival analysis](https://www.sciencedirect.com/science/article/pii/S1756231716300639)
# - [Survival analysis using R lecture slides](http://www.stat.columbia.edu/~madigan/W2025/notes/survival.pdf)
#
# ![My normal approach is useless here, too.](https://imgs.xkcd.com/comics/probability.png)
#
# <center>source: <a href="https://xkcd.com/881/">xkcd</a></center>

# #  Overview
# The aim of survival analysis is to analyze the effect of different risk factors and use them to predict the duration of time between one event ("birth") and another ("death"). It was first developed by actuaries and medical professionals to predict (as its name implies) how long individuals would survive. However, it has expanded into include many different applications.
# * it is referred to as **reliability analysis** in engineering
# * it can be referred to more generally as **time-to-event analysis**
#
# In the general sense, it can be thought of as a way to model anything with a finite duration - retention, churn, completion, etc. The culmination of this duration may have a "good" or "bad" (or "neutral") connotation, depending on the situation. However old habits die hard, so most often it is called survival analysis and the following definitions are still commonly used:
#
# * birth: the event that marks the beginning of the time period for observation
# * death: the event of interest, which then marks the end of the observation period for an individual
#
# Example | Birth Event | Death Event
# ---|---|---
# Customer churn | customer subscribes to a service| customer leaves the service
# Employee retention | employee is hired | employee quits
# Engineering, part reliability | part is put in use | part fails
# Program completion | student begins PhD program | student earns PhD
# Response time | 911 call is made | police arrive
#
# #### So... if all we're predicting here is a length of time between two events, why can't we just use regular old Linear Regression?
# Well... if you have all the data, go for it. In some situations it may be reasonably effective.
#
# #### But, data for survival times are often highly skewed and, more importantly, we don't always get a chance to observe the "death" event. The current time or other factors interfere with our ability to observe the time of the event of interest. These observations are said to be _censored_.
#
# Additionally, the occurrence or non-occurrence of an event is binary - so, while the time is continuous, the event itself is in some ways similar to a binary event in logistic regression.

# + {"id": "DSUEMY8usgwJ", "colab_type": "text", "cell_type": "markdown"}
# ## Censorship in Data
#
# Suppose a new cancer treatment is developed. Researchers select 50 individuals for the study to undergo treatment and participate in post-treatment obsesrvation.
#
# Example | Birth Event | Death Event
# ---|---|---
# Cancer survival | Participant begins trial | Participant dies due to cancer or complications of cancer
#
# During the study:
# 1. Some participants die during the course of the study--triggering their death event 
# 2. Some participants drop out or the researchers otherwise lose contact with them. The researchers have their data up until the time they dropped out, but they don't have a death event to record
# 3. Some participants are still alive at the end of the observation period. So again, researchers have their data up until some point, but there is no death event to record
#
# We only know the interval between the "birth" event and the "death" event for participants in category 1. All others we only know that they survived _up to_ a certain point.
#
# ### Dealing with Censored Data
#
# Without survival analysis, we could deal with censored data in two ways:
# * We could just treat the end of the observation period as the time of the death event
# * (Even worse) We could drop the censored data using the rationale that we have "incomplete data" for those observations
#
# But... both of these will underestimate survival rates for the purpose of the study. We **know** that all those individuals "survived" the "death event" past a certain point.
#
# Luckily, in the 1980s a pair of smarty pants named David (main author Cox and coauthor Oakes) did the hard math work to make it possible to incorporate additional features as predictive measures to survival time probabilities. (Fun fact, the one named Cox also came up with logistic regression with non-David coauthor, Joyce Snell.)
# -

# ## Hazard Function - the dangerous bathtub
#
# The hazard function represents the *instantaneous* likelihood of failure. It can be treated as a PDF (probability density function), and with real-world data comes in three typical shapes.
#
# ![Different hazard functions](https://upload.wikimedia.org/wikipedia/commons/2/25/Compsyseng17_04.jpg)
#
# Increasing and decreasing failure rate are fairly intuitive - the "bathtub" shaped is perhaps the most surprising, but actually models many real-world situations. In fact, life expectancy in general, and most threats to it, assume this shape.
#
# What the "bathtub" means is that - threats are highest at youth (e.g. infant mortality), but then decrease and stabilize at maturity, only to eventually re-emerge in old age. Many diseases primarily threaten children and elderly, and middle aged people are also more robust to physical trauma.
#
# The "bathtub" is also suitable for many non-human situations - often with reliability analysis, mechanical parts either fail early (due to manufacturing defects), or they survive and have a relatively long lifetime to eventually fail out of age and use.

# ## Survival Function (aka reliability function)
#
# It's just a (backwards) CDF!
#
# Since the hazard function can be treated as a probability density function, it makes sense to think about the corresponding cumulative distribution function (CDF). But because we're modeling time to failure, it's actually more interesting to look at the CDF backwards - this is called the complementary cumulative distribution function.
#
# In survival analysis there's a special name for it - the survival function - and it gives the probability that the object being studied will survive beyond a given time.
#
# ![4 survival functions](https://upload.wikimedia.org/wikipedia/commons/e/e0/Four_survival_functions.svg)
#
# As you can see they all start at 1 for time 0 - at the beginning, all things are alive. Then they all move down over time to eventually approach and converge to 0. The different shapes reflect the average/expected retention of a population subject to this function over time, and as such this is a particularly useful visualization when modeling overall retention/churn situations.

# ## Ways to estimate/model survival analysis - terms to be aware of
# Key Components Necessary for these models - duration, and whether observation is censored.
#
# - Kaplan Meier Estimator
# - Nelson-Aalen Estimator
# - Proportional Hazards (Cox Model, integrates covariates)
# - Additive Hazards Model (Aalen's Additive Model, when covariates are time-dependent)
#
# As with most statistics, these are all refinements of the general principles, with the math to back them up. Software packages will tend to select reasonable defaults, and allow you to use parameters to tune or select things. The math for these gets varied and deep - but feel free to [dive in](https://en.wikipedia.org/wiki/Survival_analysis) if you're curious!

# + {"id": "DSUEMY8usgwJ", "colab_type": "text", "cell_type": "markdown"}
# ## `lifelines` library
# It wasn't until 2014 that some other smart people made an implementation of survival analysis in Python called `lifelines`. 
# It is built over Pandas and follows the same conventions for usage as scikit-learn.
#
# _Additional note: scikit pushed out a survival analysis implementation last year (2018) named scikit-survival that is imported by the name `sksurv`. It's super new so it may/may not have a bunch of bugs... but if you're interested you can check it out in the future. (For comparison, scikit originally came out in 2007 and Pandas came out in 2008)._
#
# ### You can use any Pandas DataFrame with lifelines, but you must  have features for:
# * a duration of time for the observation
# * a binary column regarding censorship (`1` if the death event was observed, `0` if the death event was not observed)
#
# Sometimes, you will have to engineer these features. How might you go about that? What information would you need?
# -

# # Example 1: Leukemia
#
# `lifelines` comes with some datasets to get you started playing around with it.
#
# Most of the datasets are cleaned-up versions of real datasets. Here we will use their Leukemia dataset comparing 2 different treatments taken from http://web1.sph.emory.edu/dkleinb/allDatasets/surv2datasets/anderson.dat

# + {"id": "d51G4sPqsgww", "colab_type": "code", "outputId": "6704a8e2-79ce-4fa5-d596-88c7bec6d818", "colab": {"base_uri": "https://localhost:8080/", "height": 206}}
from lifelines.datasets import load_leukemia

leukemia = load_leukemia()

leukemia.head()

# + {"id": "DQ936c5tsgw-", "colab_type": "code", "outputId": "94d35943-a551-46c5-975e-3862872cce1e", "colab": {"base_uri": "https://localhost:8080/", "height": 191}}
leukemia.info()

# + {"id": "MDvA8Z9rsgxL", "colab_type": "code", "outputId": "0ce5b40c-0a8c-4508-990f-25ad0d0a1810", "colab": {"base_uri": "https://localhost:8080/", "height": 300}}
leukemia.describe()

# + {"id": "tDasOEocsgxQ", "colab_type": "code", "outputId": "fa606f2c-3531-4d30-d453-55f257b85a9f", "colab": {"base_uri": "https://localhost:8080/", "height": 376}}
durations = leukemia.t.values
events = leukemia.status.values

ax = lifelines.plotting.plot_lifetimes(durations=durations,
                                       event_observed=events)
ax.set_xlim(0, 40)
ax.grid(axis='x')
ax.set_xlabel("Time in Months")
ax.set_title("Lifelines for Survival of Leukemia Patients");
plt.plot();

# + {"id": "5oEzZ_aqsgxV", "colab_type": "text", "cell_type": "markdown"}
# ## Kaplan-Meier survival estimate
#  
# The Kaplan-Meier method estimates survival probability from observed survival times. It results in a step function that changes value only at the time of each event, and confidence intervals can be computed for the survival probabilities. 
#
# The **KM survival curve**, a plot of KM survival probability against time, provides a useful summary of the data.
# It can be used to estimate measures such as median survival time.
#
# It CANNOT account for risk factors and is NOT regression. It is *non-parametric* (does not involve parameters).
#
# However it is a good way to visualize a survival dataset, and can be **useful to compare the effects of a single categorical variable**.

# + {"id": "5XoM5PzGsgxX", "colab_type": "code", "outputId": "fc1070bb-1840-46d4-cc8b-1de402cf556c", "colab": {"base_uri": "https://localhost:8080/", "height": 34}}
kmf = lifelines.KaplanMeierFitter()

kmf.fit(durations, events)

kmf.survival_function_.plot()
# or kmf.survival_function_.plot.line()
plt.title('KM Survival Function: Leukemia Patients');
print(f'Median Survival: {kmf.median_} months after treatment')

# + {"id": "udKT7uBAsgxi", "colab_type": "code", "outputId": "31c095f5-70bd-4c7e-bc40-da331a449352", "colab": {"base_uri": "https://localhost:8080/", "height": 411}}
# compare the effects of a single categorical variable, "Rx"
ax = plt.subplot(111)

treatment = (leukemia["Rx"] == 1)
kmf.fit(durations=durations[treatment], 
        event_observed=events[treatment], 
        label="Treatment 1")
kmf.plot(ax=ax)
print(f'Median survival time with Treatment 1: {kmf.median_} months')

kmf.fit(durations=durations[~treatment], 
        event_observed=events[~treatment], 
        label="Treatment 0")
kmf.plot(ax=ax)
print(f'Median survival time with Treatment 0: {kmf.median_} months')

plt.ylim(0, 1);
plt.title("Survival Times for Leukemia Treatments");
# -

# **Note:** more jagged lines because of reduced sample size per group

# + {"id": "Ej1Zb4IYsgxr", "colab_type": "text", "cell_type": "markdown"}
# ## Cox Proportional Hazards Model -- Survival Regression
# Useful for comparing relative hazards (model accepts entire DataFrame).
#
# It assumes the ratio of death event risks (hazard) of two groups remains about the same over time.
# This ratio is called the hazards ratio or the relative risk.
#
# All Cox regression requires is an assumption that ratio of hazards is constant over time across groups.
#
# *The good news* — we don’t need to know anything about overall shape of risk/hazard over time
#
# *The bad news* — the proportionality assumption can be restrictive

# + {"id": "Skypo6ABsgxs", "colab_type": "code", "outputId": "7685e61e-546c-4c11-acdb-2f78a79b1d05", "colab": {"base_uri": "https://localhost:8080/", "height": 330}}
# Using Cox Proportional Hazards model
cph = lifelines.CoxPHFitter()
cph.fit(df=leukemia, duration_col='t', event_col='status')
cph.print_summary()

# + {"id": "sIUr2gT7sgxz", "colab_type": "text", "cell_type": "markdown"}
# ### Interpreting the Results
# `coef`: usually denoted with $b$, the coefficient
#
# `exp(coef)`: $e^{b}$, equals the estimate of the hazard ratio. Here, we can say that participants who received treatment 1 had ~4.5 times the hazard risk (risk of death) compared to those who received treatment 2. And for every unit the `logWBC` increased, the hazard risk increased >5 times.
#
# `se(coef)`: standard error of the coefficient (used for calculating z-score and therefore p-value)
#
# `z`: z-score $\frac{b}{se(b)}$
#
# `p`: p-value. derived from z-score. describes statistical significance. more specifically, it is the likelihood that the variable has no effect on the outcome
#
# `log(p)`: natural logarithm of p-value... used to more easily see differences in significance
#
# `lower/upper 0.95`: confidence levels for the coefficients. in this case, we can confidently say that the coefficient for `logWBC` is somewhere _between_ 1.02 and 2.34.
#
# `Signif. codes`: easily, visually identify significant variables! The more stars, the more solid (simply based on p-value). Here `logWBC` is highly significant, `Rx` is significant, and `sex` has no statistical significance
#
# `Concordance`: a measure of predictive power for classification problems (here looking at the `status` column. a value from 0 to 1 where values above 0.6 are considered good fits (the higher the better)
#
# `Likelihood ratio (LR) test`: this is a measure of how likely it is that the coefficients are not zero, and can compare the goodness of fit of a model versus an alternative null model. Is often actually calculated as a logarithm, resulting in the log-likelihood ratio statistic and allowing the distribution of the test statistic to be approximated with [Wilks' theorem](https://en.wikipedia.org/wiki/Wilks%27_theorem).

# + {"id": "SHPFMpUqsgx0", "colab_type": "code", "outputId": "6e8f47d0-1c58-437b-9908-11a7d0a44eb4", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
# investigate continuous feature, must bin with 'values'
cph.plot_covariate_groups(covariate='logWBC', values=np.arange(1.5,5,.5));

# + {"id": "hd02Nni_sgx7", "colab_type": "code", "outputId": "ababdda0-67e7-412e-8dbe-04139681e466", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
# categorical feature
cph.plot_covariate_groups(covariate='sex', values=[0,1]);

# + {"id": "-JRvblsIsgyB", "colab_type": "text", "cell_type": "markdown"}
# Check assumption that the **Cox model assumes the ratio of death events between groups remains constant over time**.

# + {"id": "XEG4bSlUsgyC", "colab_type": "code", "outputId": "289d3d97-6337-40c1-a935-8d9a1cc03f6f", "colab": {"base_uri": "https://localhost:8080/", "height": 860}}
cph.check_assumptions(leukemia)

# + {"id": "ZO_dFbKesgyG", "colab_type": "code", "outputId": "a83db192-ed8c-48d3-bbfc-9f0deb1933f9", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
# We can see that the sex variable is not very useful by plotting the coefficients
cph.plot();
# -

# Let's do what the check_assumptions function suggested:
#
# >Advice: with so few unique values (only 2), you can try  `strata=['sex']` in the call in `.fit`.

# + {"id": "D1rwy5wMsgyL", "colab_type": "code", "outputId": "dc25e7d4-dd46-4b32-b566-a33cb42a2b70", "colab": {"base_uri": "https://localhost:8080/", "height": 347}}
cph = lifelines.CoxPHFitter()
cph.fit(df=leukemia, duration_col='t', 
        event_col='status', strata=['sex'])
cph.print_summary()
cph.baseline_cumulative_hazard_.shape

# + {"id": "Qn4HZjeGsgyP", "colab_type": "text", "cell_type": "markdown"}
# This regression:
#
# `Log-likelihood ratio test = 69.61 on 2 df, -log2(p)=50.21`
#
# Regression including `sex`:
#
# `Log-likelihood ratio test = 47.19 on 3 df, -log2(p)=31.55`
#
# The `LRT` and `-log2(p)` are higher, meaning this is likely a better fitting model.

# + {"id": "jL8JzzhIsgyQ", "colab_type": "code", "outputId": "a8fc4df7-d7e1-4ca2-a31e-fff221445b84", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
cph.plot();

# + {"id": "Py4DYu_XsgyU", "colab_type": "code", "outputId": "96a4ce6f-afdd-4eb7-e071-bc69a8eff7ff", "colab": {"base_uri": "https://localhost:8080/", "height": 1367}}
cph.compute_residuals(leukemia, kind='score')

# + {"id": "LMN1uGnQsgyY", "colab_type": "code", "outputId": "de3b9044-119a-4c85-b770-0b55713b6155", "colab": {"base_uri": "https://localhost:8080/", "height": 802}}
cph.predict_cumulative_hazard(leukemia[:5])

# + {"id": "bs_Npp6osgyc", "colab_type": "code", "outputId": "8548bbfa-1576-4bea-d612-46b0ab86d7e6", "colab": {"base_uri": "https://localhost:8080/", "height": 536}}
surv_func = cph.predict_survival_function(leukemia[:5])

exp_lifetime = cph.predict_expectation(leukemia[:5])

plt.plot(surv_func)

exp_lifetime
# -

# # Example 2: Recidivism
#
# The Rossi dataset originally comes from Rossi et al. (1980), and is used as an example in Allison (1995).
#
# The data pertain to 432 convicts who were released from Maryland state prisons in the 1970s and who were followed up for one year after release. Half the released convicts were assigned at random to an experimental treatment in which they were given financial aid; half did not receive aid.

# + {"id": "z7NNzQ_5sgyh", "colab_type": "code", "outputId": "d8e0f130-4fd9-4ee8-c925-42b225fd885a", "colab": {"base_uri": "https://localhost:8080/", "height": 206}}
from lifelines.datasets import load_rossi
recidivism = load_rossi()

recidivism.head()

# Looking at the Rossi dataset, how long do you think the study lasted?

# All features are coded with numerical values, but which features do you think 
# are actually categorical?

# + {"id": "1VjqAV3ksgyk", "colab_type": "code", "outputId": "fd682c6e-d613-44d8-f3cf-1340bdfc2764", "colab": {"base_uri": "https://localhost:8080/", "height": 260}}
pd.DataFrame({'dtypes':recidivism.dtypes,
              'nunique':recidivism.nunique()})

# + {"id": "LVq_ZOFgsgyq", "colab_type": "code", "outputId": "2f893d4a-d2a2-462c-85b2-84c6c56c2da4", "colab": {"base_uri": "https://localhost:8080/", "height": 300}}
recidivism.describe()

# + {"id": "XqhPJfltsgyv", "colab_type": "code", "outputId": "c6fa9349-34fe-4c0c-cb24-d7e02fdb24d5", "colab": {"base_uri": "https://localhost:8080/", "height": 376}}
# plot "lifelines" of the study participants as they attempt to avoid recidivism
recidivism_sample = recidivism.sample(n=25)

duration = recidivism_sample.week.values
arrested = recidivism_sample.arrest.values

ax = lifelines.plotting.plot_lifetimes(duration, event_observed=arrested)
ax.set_xlim(0, 78)
ax.grid(axis='x')
ax.vlines(52, 0, 25, lw=2, linestyles='--')
ax.set_xlabel("Time in Weeks")
ax.set_title("Recidivism Rates");
plt.plot();

# + {"id": "lz4mF5kHsgy1", "colab_type": "code", "outputId": "4a0151be-2fbc-4748-db10-da7a3c4acf94", "colab": {"base_uri": "https://localhost:8080/", "height": 34}}
kmf = lifelines.KaplanMeierFitter()

duration = recidivism.week
arrested = recidivism.arrest

kmf.fit(duration, arrested)

# + {"id": "RA1FMgDNsgy4", "colab_type": "code", "outputId": "7393ed69-ecca-4961-a60c-f4c3e7123f40", "colab": {"base_uri": "https://localhost:8080/", "height": 390}}
kmf.survival_function_.plot()
plt.title('Survival Curve:\nRecidivism of Recently Released Prisoners')
plt.ylim(0,1);

# + {"id": "PXveA6jesgy8", "colab_type": "code", "outputId": "1171a85f-1fdb-4d79-a742-63c444abb7be", "colab": {"base_uri": "https://localhost:8080/", "height": 376}}
kmf.plot()
plt.title('Survival Function of Recidivism Data')
plt.ylim(0,1);

# + {"id": "Mt3ucIbgsgzB", "colab_type": "code", "outputId": "f92e392f-c9d9-466b-a212-db6c4344f1d1", "colab": {"base_uri": "https://localhost:8080/", "height": 34}}
print(f'Median time before recidivism: {kmf.median_} weeks')

# + {"id": "c9e5lAV7sgzH", "colab_type": "code", "outputId": "3c5489df-d99b-4e8d-8246-4193603365a3", "colab": {"base_uri": "https://localhost:8080/", "height": 376}}
kmf_w_aid = lifelines.KaplanMeierFitter()
kmf_no_aid = lifelines.KaplanMeierFitter()

ax = plt.subplot(111)

w_aid = (recidivism['fin']==1)

t = np.linspace(0, 70, 71)
kmf_w_aid.fit(duration[w_aid], event_observed=arrested[w_aid], 
              timeline=t, label="Received Financial Aid")
ax = kmf_w_aid.plot(ax=ax)
#print("Median survival time of democratic:", kmf.median_)

kmf_no_aid.fit(duration[~w_aid], event_observed=arrested[~w_aid], 
               timeline=t, label="No Financial Aid")
ax = kmf_no_aid.plot(ax=ax)
#print("Median survival time of non-democratic:", kmf.median_)

plt.ylim(0,1)
plt.title("Recidivism for Participants Who Received Financial Aid \nvs. Those Who Did Not");

# + {"id": "zdM4GOAOsgzN", "colab_type": "code", "outputId": "a85fa30c-4695-4e93-ffa0-a15f84e733e8", "colab": {"base_uri": "https://localhost:8080/", "height": 500}}
naf = lifelines.NelsonAalenFitter()
naf.fit(duration, arrested)

print(naf.cumulative_hazard_.head())
naf.plot();

# + {"id": "uJVPVtmYsgzR", "colab_type": "code", "outputId": "e11867c7-9a27-4c1d-833c-d07e23ffcbd4", "colab": {"base_uri": "https://localhost:8080/", "height": 403}}
naf_w_aid = lifelines.NelsonAalenFitter()
naf_no_aid = lifelines.NelsonAalenFitter()

naf_w_aid.fit(duration[w_aid], event_observed=arrested[w_aid], 
              timeline=t, label="Received Financial Aid")
ax = naf_w_aid.plot(loc=slice(0, 50))
naf_no_aid.fit(duration[~w_aid], event_observed=arrested[~w_aid], 
               timeline=t, label="No Financial Aid")
ax = naf_no_aid.plot(ax=ax, loc=slice(0, 50))
plt.title("Recidivism Cumulative Hazard\n"
          "for Participants Who Received Financial Aid \n"
          "vs. Those Who Did Not");

# + {"id": "5KbuDkxjsgzV", "colab_type": "code", "outputId": "986091a0-00af-4071-bb5a-2e3eefa81544", "colab": {"base_uri": "https://localhost:8080/", "height": 503}}
cph = lifelines.CoxPHFitter()
cph.fit(recidivism, duration_col='week', 
        event_col='arrest', show_progress=True)

cph.print_summary()

# + {"id": "QoWVH0XDsgzX", "colab_type": "code", "outputId": "c4635a1e-63e3-41ad-9d85-e6a2881d932f", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
cph.plot();

# + {"id": "r8qPQeKVsgza", "colab_type": "code", "outputId": "7fb32283-e088-43fe-d690-80f0a04e0db7", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
cph.plot_covariate_groups('fin', [0, 1]);

# + {"id": "PPSlBmp-sgzc", "colab_type": "code", "outputId": "2c8aeb86-0152-41ea-8321-a6f858f20f1d", "colab": {"base_uri": "https://localhost:8080/", "height": 378}}
cph.plot_covariate_groups('prio', [0, 5, 10, 15]);

# + {"id": "8H4IMry_sgzf", "colab_type": "code", "outputId": "b7e4d43f-7d3b-4844-e7bc-3ebe2976342e", "colab": {"base_uri": "https://localhost:8080/", "height": 206}}
r = cph.compute_residuals(recidivism, 'martingale')
r.head()

# + {"id": "iODFHl9Usgzz", "colab_type": "code", "outputId": "130437c6-b2b1-473f-f7a3-165bf7379f9b", "colab": {"base_uri": "https://localhost:8080/", "height": 1579}}
cph.check_assumptions(recidivism)

# + {"id": "Su5WdRa139yW", "colab_type": "text", "cell_type": "markdown"}
# # Example 3: Heart Attack Survival
#
# https://archive.ics.uci.edu/ml/datasets/echocardiogram

# + {"id": "4GcRG1ussgz1", "colab_type": "code", "colab": {}}
# TODO

# + {"id": "8tMyVxHRa3cQ", "colab_type": "text", "cell_type": "markdown"}
# # Example 4: Customer Churn
#
# Treselle Systems, a data consulting service, [analyzed customer churn data using logistic regression](http://www.treselle.com/blog/customer-churn-logistic-regression-with-r/). For simply modeling whether or not a customer left, logistic can work, but if we want to model the actual tenure of a customer, survival analysis is more appropriate.
#
# The "tenure" feature represents the duration that a given customer has been with them, and "churn" represents whether or not that customer left (i.e. the "event", from a survival analysis perspective).
#
# data source: https://github.com/treselle-systems/customer_churn_analysis
#
# - What features best model customer churn?
# - What would you characterize as the "warning signs" that a customer may discontinue service?
# - What actions would you recommend to this business to try to improve their customer retention?
#
# Please create at least *3* plots or visualizations to support your findings, and in general write your summary/results targeting an "interested layperson" (e.g. your hypothetical business manager) as your audience.
#
# This means that, as is often the case in data science, there isn't a single objective right answer - your goal is to *support* your answer, whatever it is, with data and reasoning.

# + {"id": "OIfMQKnSy8Zl", "colab_type": "code", "outputId": "87f6401d-352f-437d-eda8-c4021573d29c", "colab": {"base_uri": "https://localhost:8080/", "height": 342}}
churn_data = pd.read_csv('https://raw.githubusercontent.com/'
                         'treselle-systems/customer_churn_analysis/'
                         'master/WA_Fn-UseC_-Telco-Customer-Churn.csv')
churn_data.head()

# +
event_col = 'Churn'
duration_col = 'tenure'

churn_data[event_col] = churn_data[event_col].map({'No':0, 'Yes':1})

predictors = sorted(list(set(churn_data.columns) - set([event_col, duration_col])))

# + {"id": "lmGBY5fX0bmu", "colab_type": "code", "outputId": "6b57713b-fcc2-4879-a213-30da3fa3d700", "colab": {"base_uri": "https://localhost:8080/", "height": 469}}
pd.DataFrame({'dtypes':churn_data[predictors].dtypes,
              'nunique':churn_data[predictors].nunique()})
# -

# `TotalCharges` should be numeric, contains ' '

# InternetService was perfectly collienar with StreamingMovies and StreamingTV
to_dummy = ['Partner', 'InternetService', 'SeniorCitizen',
            'gender', 'Dependents', 'Contract']

for col in to_dummy:
    print(col, '\n', churn_data[col].value_counts(), 
          '\n\n', sep='')

churn_data['Contract'] = churn_data['Contract'].map({'Month-to-month':'No'})
churn_data['gender'] = churn_data['gender'].map({'Male':'No'})

for col in to_dummy:
    if 'No' in churn_data[col].unique():
        churn_data[col] = churn_data[col].map({'No':0}).fillna(1)

predictors = to_dummy

churn_data[[event_col, duration_col] + predictors].corr()

# +
cph = lifelines.CoxPHFitter()
cph.fit(churn_data[[event_col, duration_col] + predictors],
        duration_col=duration_col, event_col=event_col)

cph.print_summary()
# -

cph.plot();

# categorical feature
cph.plot_covariate_groups(covariate='Contract', values=[0,1]);

# categorical feature
cph.plot_covariate_groups(covariate='InternetService', values=[0,1]);

cph.check_assumptions(churn_data[[event_col, duration_col] + predictors])
