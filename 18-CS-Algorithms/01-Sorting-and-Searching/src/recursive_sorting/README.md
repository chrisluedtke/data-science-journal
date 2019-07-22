# A Better Way to Sort

## Divide & Conquer
>A divide-and-conquer algorithm works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.  
-Wikipedia

This approach can be very useful when sorting. By breaking up our original data set into subsets and recursively sorting each subset, we can obtain significant performance gains.

## Recursion Recap
Remember that when writing a recursive algorithm, there are two pieces we have to define:
- Base case
- Recursive case

Recursive cases *must* be written in a way that will eventually allow us to reach the base case. Otherwise, infinite recursion will lead to ***STACK OVERFLOW***!

# Recursive Sorting Algorithms

## Quick Sort
Let's think about the group photo example again. Everyone's lined up and the photographer wants to order individuals from shortest to tallest. They pull out the first person from the line and instruct everyone *shorter* than this person to position themselves on the left-hand side. Everyone *taller* than this person is instructed to move to the right-hand side. The photographer then repeats this process with the group of people on the left and the group of people on the right. This is ***Quick Sort***.

[(VIDEO) Quick-sort with Hungarian folk dance](https://www.youtube.com/watch?v=ywWBy6J5gz8)

[![(VIDEO) Quick-sort with Hungarian folk dance](https://i.ytimg.com/vi/ywWBy6J5gz8/hqdefault.jpg)](https://www.youtube.com/watch?v=ywWBy6J5gz8)


### Algorithm
```
1. Select a pivot. Often times this is the first or last element in a set. It can also be the middle.
2. Move all elements smaller than the pivot to the left. 
3. Move all elements greater than the pivot to the right.
4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
```

## Your Task
- Implement the `quick_sort()` function in the Guided Project with your TA


### Real-World Applications
While ***Quick Sort*** has "quick" in its name, it is typically not used as frequently as Merge Sort. Although it *is* quick in a best case scenario, worst case for ***Quick Sort*** is *very* bad. Because of this, it is not often chosen for production.



## Merge Sort
Your boss asks you to organize an old filing cabinet with 20 years worth of financial documents. He would like things ordered chronologically. You feel overwhelemed. There are thousands of papers in this thing.
So you decide to break this insane task up into more manageable pieces. First, you focus on organizing a single drawer. But this still has a lot of pieces of data that need to be sorted. Within the drawer, you pull out a single folder. You lay out all the contents on a table, grabbing two pieces at a time, placing the older document on top of the newer one. Then, you start merging sorted sets of documents together until the folder is done. Once all the folders have been reassembled, you order the folders correctly in the drawer. And then you put sorted drawers back into the filing cabinet. This idea of breaking a large set of data down into small pieces, sorting the pieces, then merging them back together is what ***Merge Sort*** is all about.  

[(VIDEO) Merge-sort with Transylvanian-saxon (German) folk dance](https://www.youtube.com/watch?v=XaqR3G_NVoo)  

[![(VIDEO) Merge-sort with Transylvanian-saxon (German) folk dance](https://i.ytimg.com/vi/XaqR3G_NVoo/hqdefault.jpg)](https://www.youtube.com/watch?v=XaqR3G_NVoo)


### Algorithm
```
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
```


### Real-World Applications
Have you ever wondered how some of the languages you use actually implement their built-in `sort()` functions? Many of them actually utilize the ***Merge Sort*** algorithm! *WHY* they do so is because this sorting algorithm is reliably efficient. In all cases, regardless of how sorted the original data set might be, this algorithm will have a runtime of O(n log(n)), one of the better sorting runtimes out there.

### Your Task 
- Implement `merge_sort()` in `recursive_sorting.py`. It's recommended that you use...
  - A recursive function that handles dividing the array (or subarray) in half
  - A helper function that handles merging sorted pieces back together
- ***STRETCH*** - Try writing an *in-place* ***Merge Sort*** algorithm.


## TO-DO in recursive_sorting.py
- Implement the `merge_sort()`

## Stretch Goals

### Make a better Merge Sort
- While a little more challenging, it is possible to implement ***Merge Sort*** **in-place** (without using extra memory). Try writing a second `merge_sort()` function that does this.

### Timsort is a combination of the Merge Sort and Insertion Sort algorithms.
- What programming languages use **Timsort** to implement their built-in `sort()` functions?
- If an interviewer asked you to describe the **Tim Sort** algorithm in 3-4 sentences, what would you say?
- Can you implement **Tim Sort** in Python?
