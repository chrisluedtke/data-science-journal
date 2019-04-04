# Apache Spark Assignment, Day 1 of 2

### 1. [Sign up for Databricks Community Edition](https://databricks.com/signup#signup/community)

Today we’ll continue our tour of different cloud notebook platforms!

We’ll use **Databricks Community Edition** today, because it’s:

- Free! (Unlimited credits)
- Preconfigured, convenient
- Preloaded with datasets
- Made for Spark, by its creators

### 2. [Sign in to Databricks Community Edition](https://community.cloud.databricks.com/login.html)

### 3. Explore the Quickstart tutorial

From the **Welcome to databricks** page, click on **Explore the Quickstart tutorial.**

This will open a notebook. Follow the instructions to Create a quickstart cluster, Attach the notebook to the cluster and run all commands in the notebook.

(You don't have to type the commands yourself from scratch. The purpose here is just to see a preview of what you can do with Spark and Databricks, and verify it's working for you. Note that [Databricks documentation](https://docs.databricks.com/getting-started/quick-start.html) has more information about this tutorial.)

### 4. [Create a notebook](https://docs.databricks.com/user-guide/notebooks/notebook-manage.html#create-a-notebook) (Scala)

### 5. Estimate Pi

In your notebook, run the Pi Estimation example (in Scala) from the [Apache Spark Examples](https://spark.apache.org/examples.html).

(First you'll need to assign an integer value to the `NUM_SAMPLES` constant.)

How does the code compare to the `monte_carlo_pi` example on [Numba's homepage](http://numba.pydata.org/)?

(Regarding the performance: Note that [Databricks Community Edition](https://databricks.com/try-databricks) is a "Single cluster limited to 6GB and no worker nodes.")

### 6. Do exercises from _Spark: The Definitive Guide_

First, read [_Spark: The Definitive Guide_ excerpts](https://pages.databricks.com/rs/094-YMS-629/images/Apache-Spark-The-Definitive-Guide-Excerpts-R1.pdf), **Pages 1-21.**

Then, in your notebook, do the [code exercises from _Spark: The Definitive Guide_, **Chapter 2: A Gentle Introduction to Spark**](https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_2_A_Gentle_Introduction_to_Spark.scala).

**Important!** Note these instructions from the [repo README](https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/README.md):
> Rather than you having to upload all of the data yourself, you simply have to **change the path in each chapter from `/data` to `/databricks-datasets/definitive-guide/data`**. Once you've done that, all examples should run without issue.

Next, read [_Spark: The Definitive Guide_ excerpts](https://pages.databricks.com/rs/094-YMS-629/images/Apache-Spark-The-Definitive-Guide-Excerpts-R1.pdf), **Pages 26-31.**

Then, in your notebook, do the [code exercises from _Spark: The Definitive Guide_, **Chapter 3: A Tour of Spark’s Toolset**](https://github.com/databricks/Spark-The-Definitive-Guide/blob/master/code/A_Gentle_Introduction_to_Spark-Chapter_3_A_Tour_of_Sparks_Toolset.scala), **only lines 28-105.** (You don't need to do the Datasets exercise at the beginning, or the Machine Learning exercise at the end.)

Do the exercises [**"the hard way"**](https://learnpythonthehardway.org/python3/intro.html):

> You will do the incredibly simple things that all programmers do to learn a programming language:
> 1. Go through each exercise.
> 2. Type in each _exactly._
> 3. Make it run.

### 7. Export and commit your notebook

[Export your notebook](https://docs.databricks.com/user-guide/notebooks/notebook-manage.html#export-a-notebook) as an HTML file. Commit the file to your GitHub repo.
