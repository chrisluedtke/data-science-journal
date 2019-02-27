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

# + {"id": "pAMmqTAvXVN6", "colab_type": "text", "cell_type": "markdown"}
# # Probability Density Function and Cumulative Distribution Function
#
# <https://www.math.utah.edu/~lzhang/teaching/3070summer2008/DailyUpdates/jun26/sec4_1.pdf>
#
# Recall that a **random variable** is a variable whose numerical outcomes are the process of a random phenomenon (usually random with regards to some underlying frequency distribution).
#
# Let's say we want to know the probability that the temperature at noon on a given day in June in Utah is 75&deg;F-77&deg;F. We record the temperature at Noon in Salt Lake City (the capital) on every June day for the past 20 years (giving ~600 observations) and plot histograms: 
#
# <center><img width="800" src="http://www.ryanleeallred.com/wp-content/uploads/2019/02/Histogram.png"></center>
#
# The height of each bin tells us how many (either a count or percent) observations live in that bin.
#
# Imagine that we took our original histogram and decreased the bin size until the it was infinitely small in the limit case. We end up with a smooth curved approximation of our original histogram. This is the **Probability Density Function**, and we use it to specify the probability of a random variable falling within a particular range of values.
#
# The area under the curve of a PDF has to be equal to 1 because it represents all of the possible outcomes of that random variable. With 100% likelihood the observed event will exist somewhere in that curve. In order to get an answer for how the probability of a random variable falling between a range of values, we look ad the start and end points of the range in question and calculate the area under the curve that exists between the upper and lower bounds of our range. 
#
# <center><img width="400" src="http://www.ryanleeallred.com/wp-content/uploads/2019/02/PDF-Histogram.png"/></center>
#
# What if we wanted to know the probability of a very specific temperature occuring on a given day? Something like 74.5896780&deg;F. **Given a continuous random variable, the probability of any specific single floating point value occuring approaches zero**. We call this probability its **absolute likelihood**.
#
# The **Cumulative Distribution Function** is simply the integral of the PDF. The y value of a CDF represents the area under the PDF that is less than or equal to that x value. 
#
# <https://en.wikipedia.org/wiki/Probability_density_function>
#
# <https://en.wikipedia.org/wiki/Cumulative_distribution_function>
#
# <https://en.wikipedia.org/wiki/Normal_distribution>
#
# <https://en.wikipedia.org/wiki/Probit>
#
# [Logit and Probit Functions Compared](https://www.google.com/search?q=probit+logit+function&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiJ1JiendngAhWVr54KHUZlBSgQ_AUIDigB&biw=1329&bih=910#imgrc=_)
#
# # Key Takeaways: 
#
# - The area under the curve of a PDF (within a given range) is equal to the probability of an occurence of the random variable within that range.
#
# - The CDF is the integral of the PDF. - Integrate the PDF to get the CDF, this is because the integral finds the area under curves.
#
# - For a given x value on a CDF the y value represents the probability of an event taking on a value less than or equal to x.
#
#
