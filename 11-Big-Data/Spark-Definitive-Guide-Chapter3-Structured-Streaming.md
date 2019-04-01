# [_Spark: The Definitive Guide,_ 2nd Edition](https://learning.oreilly.com/library/view/spark-the-definitive/9781491912201/)
Bill Chambers & Matei Zaharia  

## Chapter 3. A Tour of Spark’s Toolset

### Structured Streaming

Structured Streaming is a high-level API for stream processing that became production-ready in Spark 2.2. With Structured Streaming, you can take the same operations that you perform in batch mode using Spark’s structured APIs and run them in a streaming fashion. This can reduce latency and allow for incremental processing. The best thing about Structured Streaming is that it allows you to rapidly and quickly extract value out of streaming systems with virtually no code changes. It also makes it easy to conceptualize because you can write your batch job as a way to prototype it and then you can convert it to a streaming job. The way all of this works is by incrementally processing that data.

Let’s walk through a simple example of how easy it is to get started with Structured Streaming. For this, we will use a retail dataset, one that has specific dates and times for us to be able to use. We will use the “by-day” set of files, in which one file represents one day of data.

We put it in this format to simulate data being produced in a consistent and regular manner by a different process. This is retail data so imagine that these are being produced by retail stores and sent to a location where they will be read by our Structured Streaming job.

It’s also worth sharing a sample of the data so you can reference what the data looks like:

```
InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,2010-12-01 08:26:00,2.55,17...
536365,71053,WHITE METAL LANTERN,6,2010-12-01 08:26:00,3.39,17850.0,United Kin...
536365,84406B,CREAM CUPID HEARTS COAT HANGER,8,2010-12-01 08:26:00,2.75,17850...
```

To ground this, let’s first analyze the data as a static dataset and create a DataFrame to do so. We’ll also create a schema from this static dataset (there are ways of using schema inference with streaming that we will touch on in Part V):

```scala
val staticDataFrame = spark.read.format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/databricks-datasets/definitive-guide/data/retail-data/by-day/*.csv")

staticDataFrame.createOrReplaceTempView("retail_data")
val staticSchema = staticDataFrame.schema
```

Because we’re working with time–series data, it’s worth mentioning how we might go along grouping and aggregating our data. In this example we’ll take a look at the sale hours during which a given customer (identified by CustomerId) makes a large purchase. For example, let’s add a total cost column and see on what days a customer spent the most.

The window function will include all data from each day in the aggregation. It’s simply a window over the time–series column in our data. This is a helpful tool for manipulating date and timestamps because we can specify our requirements in a more human form (via intervals), and Spark will group all of them together for us:

```scala
import org.apache.spark.sql.functions.{window, column, desc, col}
staticDataFrame
  .selectExpr(
    "CustomerId",
    "(UnitPrice * Quantity) as total_cost",
    "InvoiceDate")
  .groupBy(
    col("CustomerId"), window(col("InvoiceDate"), "1 day"))
  .sum("total_cost")
  .show(5)
```

It’s worth mentioning that you can also run this as SQL code, just as we saw in the previous chapter.

Here’s a sample of the output that you’ll see:

```
+----------+--------------------+------------------+
|CustomerId|              window|   sum(total_cost)|
+----------+--------------------+------------------+
|   17450.0|[2011-09-20 00:00...|          71601.44|
...
|      null|[2011-12-08 00:00...|31975.590000000007|
+----------+--------------------+------------------+
```

The null values represent the fact that we don’t have a customerId for some transactions.

That’s the static DataFrame version; there shouldn’t be any big surprises in there if you’re familiar with the syntax.

Because you’re likely running this in local mode, it’s a good practice to set the number of shuffle partitions to something that’s going to be a better fit for local mode. This configuration specifies the number of partitions that should be created after a shuffle. By default, the value is 200, but because there aren’t many executors on this machine, it’s worth reducing this to 5. We did this same operation in Chapter 2, so if you don’t remember why this is important, feel free to flip back to review.

```scala
spark.conf.set("spark.sql.shuffle.partitions", "5")
```

Now that we’ve seen how that works, let’s take a look at the streaming code! You’ll notice that very little actually changes about the code. The biggest change is that we used readStream instead of read, additionally you’ll notice the maxFilesPerTrigger option, which simply specifies the number of files we should read in at once. This is to make our demonstration more “streaming,” and in a production scenario this would probably be omitted.

```scala
val streamingDataFrame = spark.readStream
    .schema(staticSchema)
    .option("maxFilesPerTrigger", 1)
    .format("csv")
    .option("header", "true")
    .load("/databricks-datasets/definitive-guide/data/retail-data/by-day/*.csv")
```

Now we can see whether our DataFrame is streaming:

```scala
streamingDataFrame.isStreaming // returns true
```

Let’s set up the same business logic as the previous DataFrame manipulation. We’ll perform a summation in the process:

```scala
val purchaseByCustomerPerHour = streamingDataFrame
  .selectExpr(
    "CustomerId",
    "(UnitPrice * Quantity) as total_cost",
    "InvoiceDate")
  .groupBy(
    $"CustomerId", window($"InvoiceDate", "1 day"))
  .sum("total_cost")
```

This is still a lazy operation, so we will need to call a streaming action to start the execution of this data flow.

Streaming actions are a bit different from our conventional static action because we’re going to be populating data somewhere instead of just calling something like count (which doesn’t make any sense on a stream anyways). The action we will use will output to an in-memory table that we will update after each trigger. In this case, each trigger is based on an individual file (the read option that we set). Spark will mutate the data in the in-memory table such that we will always have the highest value as specified in our previous aggregation:

```scala
purchaseByCustomerPerHour.writeStream
    .format("memory") // memory = store in-memory table
    .queryName("customer_purchases") // the name of the in-memory table
    .outputMode("complete") // complete = all the counts should be in the table
    .start()
```

When we start the stream, we can run queries against it to debug what our result will look like if we were to write this out to a production sink:

```scala
spark.sql("""
  SELECT *
  FROM customer_purchases
  ORDER BY `sum(total_cost)` DESC
  """)
  .show(5)
```

You’ll notice that the composition of our table changes as we read in more data! With each file, the results might or might not be changing based on the data. Naturally, because we’re grouping customers, we hope to see an increase in the top customer purchase amounts over time (and do for a period of time!). Another option you can use is to write the results out to the console:

```scala
purchaseByCustomerPerHour.writeStream
    .format("console")
    .queryName("customer_purchases_2")
    .outputMode("complete")
    .start()
```

You shouldn’t use either of these streaming methods in production, but they do make for convenient demonstration of Structured Streaming’s power. Notice how this window is built on event time, as well, not the time at which Spark processes the data. This was one of the shortcomings of Spark Streaming that Structured Streaming has resolved. We cover Structured Streaming in depth in Part V.
