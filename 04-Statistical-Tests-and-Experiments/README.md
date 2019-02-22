###### Unit 1: Descriptive Statistics, Sprint 4: Statistical Tests and Experiments

## Probability, Statistics, and Inference
Statistics is, in some ways, the most tolerant branch of mathematics - unlike its kin, statistics accepts situations where the exact and complete are unattainable. We’ve learned about the basic summary metrics provided by descriptive statistics - mean, median, mode, standard deviation - and how these can be represented both numerically and visually to help tell a story about data.

In this module we’ll still use these metrics, but go deeper into their meaning and interpretation, in order to perform hypothesis tests that allow us to state with “confidence” conclusions about our data. We’ll also learn about the foundations of statistics - probability and set theory - where the pure mathematics comes from.

As with all data science, there are many methods here, and we will cover the solid foundation and most generally useful tools.

#### Objectives:
* Student should be able to demonstrate understanding of fundamental concepts of set theory and probability, including permutations, combinations, expected value, variance, binomial distribution, and Bernoulli trial
* Student should be able to explain the importance of statistics in the context of informing a practical and reliable understanding of data

## Sampling, Confidence Intervals and Hypothesis Testing
In this module, we will cover sampling and other key topics related to sampling such as confidence intervals and hypothesis testing. Sampling is a process that is related to the selection of individual observations; it helps us make statistical inferences about the population. Accumulating all the information about the population (a census) is time consuming and expensive. Therefore, sampling is performed to make inferences about the population. In sampling, we assume that samples are drawn from the population and sample means and population means are equal.

Given that a sample is a group of individual observations drawn from a population, the # of individual units or observations that constitute a sample is known as the sample size. Since the intent of the sample is to provide a representative picture of the entire population, the larger the sample size, the more accurate is the measurement and the more confidence we have that the sample is actually representative of the whole population.

We will delve further into sampling and sample sizes which will help us grasp the topic: What is the standard error of a sample? Let’s say we have a distribution of continuous random variables. From the distribution, we take a sample of 10 observations and plot the average of the 10 observations.

We repeat this exercise several times, on each occasion we gather a sample of 10 observations from the distribution and plot the average of the 10 observations. As we keep repeating this exercise, the sampling distribution of the sample mean will represent a normal distribution.

If we were to repeat the entire exercise with larger sample sizes, the curve would become narrower, taller and the standard deviation would be tighter. You will notice that with larger sample sizes, the sample mean will approach the population mean. The Standard Error (SE) tells you how far your sample mean deviates from the population mean.

Remember, the larger your sample size, the closer your sample mean is to the actual population mean. Note that the Standard Error is very similar to the Standard Deviation. Both are measures of spread. The higher the number, the more spread out your data is.

However, there is a key difference between the Standard Error and Standard Deviation. The standard error uses statistics (i.e. sample data) whereas the standard deviation uses population data. The standard deviation of the sampling distribution of the sample mean is also called the standard error of the mean and is computed as follows: sd of sampling distribution of sample mean/square of n (i.e. sample size).

#### Objectives:
* Student should be able to use hypothesis testing to determine an outcome is significant or just the result of chance
* Student should be able to determine the level of confidence for a possible outcome

## Introduction to Bayesian Inference
So far all statistics we’ve studied is actually called frequentist statistics - drawing conclusions about a complete population or process by generalizing from the frequency or proportion of observed data. Frequentist statistics is well-established, and is still the default in most situations - but Bayesian statistics is an increasingly popular approach, and arguably better model for our brains and how we actually form and update beliefs based on evidence.

#### Objectives:
* Student should be able to be able to derive Bayes' theorem from the Law of Conditional Probability
* Student should be able to calculate Bayesian confidence intervals

## Real-world Experiment Design
Math is hard, but the real world is harder - you’ve learned how to perform and evaluate hypotheses tests on data, but what’s truly interesting in this domain is to be able to gather your own data for testing. As you know from earlier weeks, gathering and cleaning data is generally non-trivial, but it’s even trickier when you want to use it to fairly and robustly test various hypotheses.

In this module we will consider this challenge - how do we design and run an experiment? We will generally focus on web applications as a domain, but these techniques can be applied to any number of products, and indeed scientific scenarios more broadly. There are particular challenges working in the “real-world” though, and we will highlight those.

#### Objectives:
* Student should be able to deploy a simple static (front-end) A/B-instrumented webpage
* Student should be able to evaluate and summarize findings from real-world A/B test data
