_Lambda School Data Science - Big Data_

# Scala for Spark - Assignment

### Learn Scala the Hard Way

[**Create an Amazon EMR Notebook**](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-create.html). When creating your notebook, choose **Create a Cluster**, with 1 m4.large instance.

[From the **Kernel** menu, choose **Change kernel**](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-working-with.html) and then select the **Spark** kernel. This enables you to use the Scala programming language.

Then do the exercises below, which come from [**Learn X in Y minutes, Where X=Scala**](https://learnxinyminutes.com/docs/scala/). _(This is most of parts 1-4, 7, 9.)_

Do it [**"the hard way"**](https://learnpythonthehardway.org/python3/intro.html):

> You will do the incredibly simple things that all programmers do to learn a programming language:
> 1. Go through each exercise.
> 2. Type in each _exactly._
> 3. Make it run.

When you're done, from the **File** menu, choose **Download as Notebook (.ipynb)**. Commit the file to your GitHub repo.

```scala

/*
  Try the REPL

  Scala has a tool called the REPL (Read-Eval-Print Loop) that is analogous to
  commandline interpreters in many other languages. You may type any Scala
  expression, and the result will be evaluated and printed.  

  The REPL is a very handy tool to test and verify code.  Use it as you read
  this tutorial to quickly explore concepts on your own.
*/


/////////////////////////////////////////////////
// 1. Basics
/////////////////////////////////////////////////

// Single-line comments start with two forward slashes

/*
  Multi-line comments, as you can already see from above, look like this.
*/

// Printing, and forcing a new line on the next print
println("Hello world!")
println(10)
// Hello world!
// 10

// Printing, without forcing a new line on next print
print("Hello world")
print(10)
// Hello world10

// Declaring values is done using either var or val.
// val declarations are immutable, whereas vars are mutable. Immutability is
// a good thing.
val x = 10 // x is now 10
x = 20     // error: reassignment to val
var y = 10
y = 20     // y is now 20

/*
  Scala is a statically typed language, yet note that in the above declarations,
  we did not specify a type. This is due to a language feature called type
  inference. In most cases, Scala compiler can guess what the type of a variable
  is, so you don't have to type it every time. We can explicitly declare the
  type of a variable like so:
*/
val z: Int = 10
val a: Double = 1.0

// Notice automatic conversion from Int to Double, result is 10.0, not 10
val b: Double = 10

// Boolean values
true
false

// Boolean operations
!true         // false
!false        // true
true == false // false
10 > 5        // true

// Math is as per usual
1 + 1   // 2
2 - 1   // 1
5 * 3   // 15
6 / 2   // 3
6 / 4   // 1
6.0 / 4 // 1.5
6 / 4.0 // 1.5


// Evaluating an expression in the REPL gives you the type and value of the result

1 + 7

/* The above line results in:

  scala> 1 + 7
  res29: Int = 8

  This means the result of evaluating 1 + 7 is an object of type Int with a
  value of 8

  Note that "res29" is a sequentially generated variable name to store the
  results of the expressions you typed, your output may differ.
*/

"Scala strings are surrounded by double quotes"
'a' // A Scala Char
// 'Single quote strings don't exist' <= This causes an error

// Strings have the usual Java methods defined on them
"hello world".length
"hello world".substring(2, 6)
"hello world".replace("C", "3")

// They also have some extra Scala methods. See also: scala.collection.immutable.StringOps
"hello world".take(5)
"hello world".drop(5)

// String interpolation: notice the prefix "s"
val n = 45
s"We have $n apples" // => "We have 45 apples"

// Expressions inside interpolated strings are also possible
s"Power of 2: ${math.pow(2, 2)}"                      // => "Power of 2: 4"

// Some characters need to be "escaped", e.g. a double quote inside a string:
"They stood outside the \"Rose and Crown\"" // => "They stood outside the "Rose and Crown""


/////////////////////////////////////////////////
// 2. Functions
/////////////////////////////////////////////////

// Functions are defined like so:
//
//   def functionName(args...): ReturnType = { body... }
//
// If you come from more traditional languages, notice the omission of the
// return keyword. In Scala, the last expression in the function block is the
// return value.
def sumOfSquares(x: Int, y: Int): Int = {
  val x2 = x * x
  val y2 = y * y
  x2 + y2
}

// The { } can be omitted if the function body is a single expression:
def sumOfSquaresShort(x: Int, y: Int): Int = x * x + y * y

// Syntax for calling functions is familiar:
sumOfSquares(3, 4)  // => 25

// You can use parameters names to specify them in different order
def subtract(x: Int, y: Int): Int = x - y

subtract(10, 3)     // => 7
subtract(y=10, x=3) // => -7

// In most cases (with recursive functions the most notable exception), function
// return type can be omitted, and the same type inference we saw with variables
// will work with function return values:
def sq(x: Int) = x * x  // Compiler can guess return type is Int

// Functions can have default parameters:
def addWithDefault(x: Int, y: Int = 5) = x + y
addWithDefault(1, 2) // => 3
addWithDefault(1)    // => 6


// Anonymous functions look like this:
(x: Int) => x * x

// Unlike defs, even the input type of anonymous functions can be omitted if the
// context makes it clear. Notice the type "Int => Int" which means a function
// that takes Int and returns Int.
val sq: Int => Int = x => x * x

// Anonymous functions can be called as usual:
sq(10)   // => 100

// If each argument in your anonymous function is
// used only once, Scala gives you an even shorter way to define them. These
// anonymous functions turn out to be extremely common, as will be obvious in
// the data structure section.
val addOne: Int => Int = _ + 1
val weirdSum: (Int, Int) => Int = (_ * 2 + _ * 3)

addOne(5)      // => 6
weirdSum(2, 4) // => 16


/////////////////////////////////////////////////
// 3. Flow Control
/////////////////////////////////////////////////

1 to 5
val r = 1 to 5
r.foreach(println)

r foreach println
// NB: Scala is quite lenient when it comes to dots and brackets - study the
// rules separately. This helps write DSLs and APIs that read like English

// Why doesn't `println` need any parameters here?
// Stay tuned for first-class functions in the Functional Programming section below!
(5 to 1 by -1) foreach (println)


// Recursion is the idiomatic way of repeating an action in Scala (as in most
// other functional languages).
// Recursive functions need an explicit return type, the compiler can't infer it.
// Here it's Unit, which is analagous to a `void` return type in Java
def showNumbersInRange(a: Int, b: Int): Unit = {
  print(a)
  if (a < b)
    showNumbersInRange(a + 1, b)
}
showNumbersInRange(1, 14)


// Conditionals

val x = 10

if (x == 1) println("yeah")
if (x == 10) println("yeah")
if (x == 11) println("yeah")
if (x == 11) println("yeah") else println("nay")

println(if (x == 10) "yeah" else "nope")
val text = if (x == 10) "yeah" else "nope"


/////////////////////////////////////////////////
// 4. Data Structures
/////////////////////////////////////////////////

val a = Array(1, 2, 3, 5, 8, 13)
a(0)     // Int = 1
a(3)     // Int = 5
a(21)    // Throws an exception

val s = Set(1, 3, 7)
s(0)      // Boolean = false
s(1)      // Boolean = true


// Tuples

(1, 2)

(4, 3, 2)

(1, 2, "three")

(a, 2, "three")

// Why have this?
val divideInts = (x: Int, y: Int) => (x / y, x % y)

// The function divideInts gives you the result and the remainder
divideInts(10, 3)    // (Int, Int) = (3,1)

// To access the elements of a tuple, use _._n where n is the 1-based index of
// the element
val d = divideInts(10, 3)    // (Int, Int) = (3,1)

d._1    // Int = 3
d._2    // Int = 1

// Alternatively you can do multiple-variable assignment to tuple, which is more
// convenient and readable in many cases
val (div, mod) = divideInts(10, 3)

div     // Int = 3
mod     // Int = 1


/////////////////////////////////////////////////
// 7. Functional Programming
/////////////////////////////////////////////////

// Scala allows methods and functions to return, or take as parameters, other
// functions or methods.

val add10: Int => Int = _ + 10 // A function taking an Int and returning an Int
List(1, 2, 3) map add10 // List(11, 12, 13) - add10 is applied to each element

// Anonymous functions can be used instead of named functions:
List(1, 2, 3) map (x => x + 10)

// And the underscore symbol, can be used if there is just one argument to the
// anonymous function. It gets bound as the variable
List(1, 2, 3) map (_ + 10)

// If the anonymous block AND the function you are applying both take one
// argument, you can even omit the underscore
List("Dom", "Bob", "Natalia") foreach println


// Combinators
// Using `s` from above:
// val s = Set(1, 3, 7)

s.map(sq)

val sSquared = s. map(sq)

sSquared.filter(_ < 10)

sSquared.reduce (_+_)

// The filter function takes a predicate (a function from A -> Boolean) and
// selects all elements which satisfy the predicate
List(1, 2, 3) filter (_ > 2) // List(3)
case class Person(name: String, age: Int)
List(
  Person(name = "Dom", age = 23),
  Person(name = "Bob", age = 30)
).filter(_.age > 25) // List(Person("Bob", 30))


// Certain collections (such as List) in Scala have a `foreach` method,
// which takes as an argument a type returning Unit - that is, a void method
val aListOfNumbers = List(1, 2, 3, 4, 10, 20, 100)
aListOfNumbers foreach (x => println(x))
aListOfNumbers foreach println


/////////////////////////////////////////////////
// 9. Misc
/////////////////////////////////////////////////

// Importing things
import scala.collection.immutable.List

// Import all "sub packages"
import scala.collection.immutable._

// Import multiple classes in one statement
import scala.collection.immutable.{List, Map}

// Rename an import using '=>'
import scala.collection.immutable.{List => ImmutableList}

```

# Stretch Challenges
- http://ampcamp.berkeley.edu/big-data-mini-course/introduction-to-the-scala-shell.html
- https://www.scala-exercises.org/scala_tutorial
- https://www.hackerrank.com/domains/fp

Aaron recommends [this course from the creator of Scala](https://www.coursera.org/learn/progfun1)!
> First in a series (of 3) courses on Scala, taught by Martin Odersky - the creator of Scala. So, super interesting and high quality, and a good introduction to functional programming. Overall Scala is a large language (more things in it than Python), but people who like it usually stick to the more functional/immutable subset.
