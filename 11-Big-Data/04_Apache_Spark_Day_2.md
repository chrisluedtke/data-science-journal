_Lambda School Data Science - Big Data_

# Apache Spark, day 2 — lesson

Today we’ll continue using Databricks Community Edition. [Sign in](https://community.cloud.databricks.com/login.html) and [create a notebook](https://docs.databricks.com/user-guide/notebooks/notebook-manage.html#create-a-notebook).

## Streaming

[Here's a more complete & clear explanation of the Structured Streaming example](spark-definitive-guide-chapter3-structured-streaming.md) from yesterday's assignment.

In your Databricks notebook, click the toggle arrow next to the green animated icon, to see these streaming visualizations:

![](https://i.imgur.com/MRRHZQX.png)

## Question 1

> When we read a dataset into Spark/Scala, is there a way to see first few rows (like `.head()` in pandas)? Just to see the column names and type? — [M](https://lambdaschoolstudents.slack.com/archives/CDRMHRX2M/p1551324171174100) 


```scala
val df = spark.read.json("/databricks-datasets/samples/people/people.json")
```
<sup>https://docs.databricks.com/getting-started/spark/datasets.html#load-sample-data</sup>

```scala
df.show()
```
<sup>https://spark.apache.org/docs/latest/sql-getting-started.html#creating-dataframes</sup>

```scala
// Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")

val sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()
```
<sup>https://spark.apache.org/docs/latest/sql-getting-started.html#running-sql-queries-programmatically</sup>

```scala
// Print the schema in a tree format
df.printSchema()

// Select only the "name" column
df.select("name").show()

// Count people by age
df.groupBy("age").count().show()
```
<sup>https://spark.apache.org/docs/latest/sql-getting-started.html#untyped-dataset-operations-aka-dataframe-operations</sup>

```scala
// This import is needed to use the $-notation
import spark.implicits._

// Select everybody, but increment the age by 1
df.select($"name", $"age" + 1).show()

// Select people older than 21
df.filter($"age" > 21).show()
```
<sup>https://spark.apache.org/docs/latest/sql-getting-started.html#untyped-dataset-operations-aka-dataframe-operations</sup>

```scala
// display the dataset table just read in from the JSON file
display(df)

// Using the standard Spark commands, take() and foreach(), print the first rows
df.take(3).foreach(println(_))
```
<sup>https://docs.databricks.com/getting-started/spark/datasets.html#view-the-dataset</sup>

```scala
// range of 100 numbers to create a Dataset.
val range100 = spark.range(100)
range100.collect()
```
<sup>https://docs.databricks.com/getting-started/spark/datasets.html#create-sample-data</sup>

## Question 2

> Need help in understanding this construct...
  `.filter(vAndD => vAndD.valueDoubled % 2 == 0)` — [S](https://lambdaschoolstudents.slack.com/archives/CDRMHRX2M/p1551314845169000) 

```scala
case class ValueAndDouble(value:Long, valueDoubled:Long)

spark.range(2000)
.map(value => ValueAndDouble(value, value * 2))
.filter(vAndD => vAndD.valueDoubled % 2 == 0)
.where("value % 3 = 0")
.count()
```
<sup>https://pages.databricks.com/rs/094-YMS-629/images/Apache-Spark-The-Definitive-Guide-Excerpts-R1.pdf page 23</sup>

> not a scala post but ultra relevant and maybe helpful: [Modern Pandas: Method Chaining](https://tomaugspurger.github.io/method-chaining) — [Q](https://lambdaschoolstudents.slack.com/archives/CDRMHRX2M/p1551325239176800)

To understand chains, add and remove parts in an interactive REPL shell. For example:

```scala
// Iteration 1 - use less data 
case class ValueAndDouble(value:Long, valueDoubled:Long)
spark.range(20)  // changed 2000 to 20
.map(value => ValueAndDouble(value, value * 2))
.filter(vAndD => vAndD.valueDoubled % 2 == 0)
.where("value % 3 = 0")
.count()

// Iteration 2 - look at the data
case class ValueAndDouble(value:Long, valueDoubled:Long)
spark.range(20)
.map(value => ValueAndDouble(value, value * 2))
.filter(vAndD => vAndD.valueDoubled % 2 == 0)
.where("value % 3 = 0")
.collect()  // changed count to collect

// Iteration 3 - remove almost all the lines
spark.range(20)
.collect()

// Iteration 4 - add back part of the next line
spark.range(20)
.map(value => (value, value * 2))
.collect()

// Iteration 5 - repeat
spark.range(20)
.map(value => (value, value * 2))
.filter(vAndD => vAndD._2 % 2 == 0)
.collect()

// Iteration 6 - repeat 
spark.range(20)
.map(value => (value, value * 2))
.filter(vAndD => vAndD._2 % 2 == 0)
.where("_1 % 3 = 0")
.collect()

// Then back to Iteration 2, Iteration 1, & Original example
```

## Assignment

Use this Databricks dataset:

```
/databricks-datasets/data.gov/farmers_markets_geographic_data/data-001/market_data.csv
```

[Load the data](https://docs.databricks.com/user-guide/importing-data.html#load-data) into a Spark dataframe. Infer the schema and include the header.

How many columns does this dataframe have? How many rows?

How many farmer's markets are in your zip code? In your state? In the country?

What farmer's market has the longest name?

What are the top ten states with the most farmer's markets? 

[Display visualizations](https://docs.databricks.com/user-guide/visualizations/index.html). Explore plot options.

[Export your notebook](https://docs.databricks.com/user-guide/notebooks/notebook-manage.html#export-a-notebook) as an HTML file. Commit the file to your GitHub repo. (You can use [nbviewer](https://nbviewer.jupyter.org/) to view your HTML file on GitHub.)

## Stretch Goals

[Explore Databricks datasets](https://docs.databricks.com/user-guide/faq/databricks-datasets.html). Choose one and do exploratory data analysis.

Continue reading [_Spark: The Definitive Guide_, 2nd Edition](https://learning.oreilly.com/library/view/spark-the-definitive/9781491912201/). You may want to [start a 10-day free trial of Safari Books Online](https://learning.oreilly.com/register/). Or you may be able to access Safari Books Online for free, through your local library.

Continue to do [code exercises from the book](https://github.com/databricks/Spark-The-Definitive-Guide/). Remember these instructions from the repo README:
> Rather than you having to upload all of the data yourself, you simply have to **change the path in each chapter from `/data` to `/databricks-datasets/definitive-guide/data`**. Once you've done that, all examples should run without issue.
