# Data Structures

Resources
* [Data Structures for  Coding Interviews](https://www.interviewcake.com/article/python/data-structures-coding-interview?course=dsa)
* [Introduction to Binary Heaps (MaxHeaps)](https://www.youtube.com/watch?v=WCm3TqScBM8)

Topics:
1. Queues
1. Doubly Linked Lists
1. Binary Search Trees
1. Heaps

Stretch Goals:
1. Generic Heaps
1. AVL Trees
1. LRU Caches

## Tasks
1. Implement each data structure, starting with the queue. Make sure you're in the approriate directory, then run `python3 test_[NAME OF DATA STRUCTURE].py` to run the tests for that data structure and check your progress. Get all the tests passing for each data structure.

2. Open up the `Data_Structures_Questions.md` file, which asks you to evaluate the runtime complexity of each of the methods you implemented for each data structure. Add your answers to each of the questions in the file.

> NOTE: The quickest and easiest way to reliably import a file in Python is to just copy and paste the file you want to import into the same directory as the file that wants to import. This obviously isn't considered best practice, but it is the most reliable way to do it across all platforms.

### Arrays
A **short integer** is an 8-bit. For example we'll use an unsigned "super-short" 4-bit memory integer. Here are numbers 1, 2, 3, 4.
```
0 0 0 0 
0 0 0 1
0 0 1 0 
0 0 1 1
```
What if we have something more extreme? To make an array we must first allocate memory for it. If we have 5 4-bit integers, we need 20 blocks, and we would fill them like above:
```
0 0 0 0 0 0 0 1 0 0 1 0 0 0 1 1
```
How would we look up values? If we wanted `array[3]` we compute `3 index * 4 bits = 12 location in memory`.
In python, arrays start at `0` because `0 index * 4 bits = 0 location in memory`, which is the start.
Arrays have to be continuous. We can't simply remove an item, we would have to represent it as:
```
0 0 0 0
```
Or we could "shift" all the array items down to cover up the spot of the item we wanted to delete. We would then have to mark the last 4 bits as not in use.

### Stacks
**Stacks** are a linear data structure that follows LIFO (Last In, First Out). They are used when the most recent thing is the most important.

Examples:
* maze traversal
* recursive stack trace

Should have methods:
* `push(item)` adds an item to the top of the stack
* `pop()` moves the item on the top of ths tack and typically returns the item that is removed
* `peek()` returns the value of the item on the top of ht estack without removing it

### Queues
**Queues** are a linear data structure that follows FIFO (First In, First Out). Opposite of stack.

Examples
* line of people at a store/bank/theater
* selling produce (sell them in the order you acquired them to minimize expired goods)
* music playlist

Should have the methods: `enqueue`, `dequeue`, and `len`.
* `enqueue` should add an item to the back of the queue.
* `dequeue` should remove and return an item from the front of the queue.
* `len` returns the number of items in the queue.
 
![Image of Queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/600px-Data_Queue.svg.png)

### Linked Lists
**Linked Lists** are a linear data structure composed of nodes connected in sequence. While arrays store and index elements contiguously, each element of a linked list is stored in a node. Unlike arrays, in which items can be accessed directly by index, items in a linked list only have reference (or a 'pointer') to the *next* item, so they can only be traversed in one direction. In this way, linked lists describe lists of things in a recursive fashion, while arrays describe lists of things in an iterative fashion.

```python
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    # the above is all you need, but here are
    # some nice accessors:
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    # a nice mutator:
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # methods to add to list
    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head:  # so we can first add to head or tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head:  # so we can first add to head or tail
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            self.head = new_node
            self.head.set_next(temp_node)

    # method to find in list
    def contains(self, value):
        if not self.head:  # if no head, list is empty, cannot contain our v
            return False

        current = self.head
        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
```

### Doubly Linked Lists
Double linked lists are useful for situations in which the space is dynamic. If we knew how much space was needed for our problem, we would be better off with an array. Doubly linked lists require more space for each element than a linked list, and their operations (e.g. insertion, deletion) are more complex since they have to deal with two references. However doubly link lists allow traversing the list in forward and backward directions.

Examples
* text buffers

* The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
* The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.
    * `add_to_head` replaces the head of the list with a new value that is passed in.
    * `add_to_tail` replaces the tail of the list with a new value that is passed in.
    * `remove_from_head` removes the head node and returns the value stored in it.
    * `remove_from_tail` removes the tail node and returns the value stored in it.
    * `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down. 
    * `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up. 
    * `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
    * `get_max` returns the maximum value in the list. 
* The `head` property is a reference to the first node and the `tail` property is a reference to the last node.

![Image of Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/610px-Doubly-linked-list.svg.png)

### Binary Search Trees

**Binary Trees** simply require that each node has no more than 2 children. **Binary Search Trees** require that each node have no more than 2 children **and** all left children have values less than their parents, all right children have values greater than their parents.

* Should have the methods `insert`, `contains`, `get_max`.
    * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
    * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
    * `get_max` returns the maximum value in the binary search tree.
    * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work.

![Image of Binary Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/300px-Binary_search_tree.svg.png)

### Heaps
**Heaps** are binary tree data structures implemented as an array. For any node in the heap, the value of the node is larger than the values of its children nodes. Therefore the root of the tree is the largest value.

**Heaps** are implemented as arrays in order to take advantage of constant-time access to any element in the heap, which also allows us to more easily swap elements in different positions throughout the heap. To traverse the tree, we use formulaic look-up methods. Given a parent node's index value, `i`, the parent's left child index is `2i + 1`, and its right child is located at index `2i + 2`. Conversely,a node's parent is located at index `floor((i - 1) / 2)`.

* **Heaps** have the following constraints 
    1. each node is greater than each of its children (in generic heap)
    1. the tree is perfectly balanced
    1. all leaves are in the leftmost position available.

* Should have the methods `insert`, `delete`, `get_max`, `_bubble_up`, and `_sift_down`.
    * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
    * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed. 
    * `get_max` returns the maximum value in the heap _in constant time_.
    * `get_size` returns the number of elements stored in the heap.
    * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
    * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.

![Image of a Heap in Tree form](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Max-Heap.svg/501px-Max-Heap.svg.png)

![Image of a Heap in Array form](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Heap-as-array.svg/603px-Heap-as-array.svg.png)

## Stretch Goals

### Generic Heaps
A max heap is pretty useful, but what's even more useful is to have our heap be generic such that the user can define their own priority function and pass it to the heap to use.

Augment your heap implementation so that it exhibits this behavior. If no comparator function is passed in to the heap constructor, it should default to being a max heap. Also change the name of the `get_max` function to `get_priority`.

You can test your implementation against the tests in `test_generic_heap.py`. The test expects your augmented heap implementation lives in a file called `generic_heap.py`. Feel free to change the import statement to work with your file structure or copy/paste your implementation into a file with the expected name. 

### AVL Tree
An AVL tree (Georgy Adelson-Velsky and Landis' tree, named after the inventors) is a self-balancing binary search tree. In an AVL tree, the heights of the two child subtrees of any node differ by at most one; if at any time they differ by more than one, rebalancing is done to restore this property.

We define balance factor for each node as :
```
balanceFactor = height(left subtree) - height(right subtree)
```

The balance factor of any node of an AVL tree is in the integer range [-1,+1]. If after any modification in the tree, the balance factor becomes less than −1 or greater than +1, the subtree rooted at this node is unbalanced, and a rotation is needed.

![AVL tree rebalancing](https://s3.amazonaws.com/hr-challenge-images/0/1436854305-b167cc766c-AVL_Tree_Rebalancing.svg.png)

Implement an AVL Tree class that exhibits the aforementioned behavior. The tree's `insert` method should perform the same logic as what was implemented for the binary search tree, with the caveat that upon inserting a new element into the tree, it will then check to see if the tree needs to be rebalanced. 

How does the time complexity of the AVL Tree's insertion method differ from the binary search tree's?

### LRU Cache
An LRU (Least Recently Used) cache is an in-memory storage structure that adheres to the [Least Recently Used](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)) caching strategy. 

In essence, you can think of an LRU cache as a data structure that keeps track of the order in which elements (which take the form of key-value pairs) it holds are added and updated. The cache also has a max number of entries it can hold. This is important because once the cache is holding the max number of entries, if a new entry is to be inserted, another pre-existing entry needs to be evicted from the cache. Because the cache is using a least-recently used strategy, the oldest entry (the one that was added/updated the longest time ago) is removed to make space for the new entry. 

So what operations will we need on our cache? We'll certainly need some sort of `set` operation to add key-value pairs to the cache. Newly-set pairs will get moved up the priority order such that every other pair in the cache is now one spot lower in the priority order that the cache maintains. The lowest-priority pair will get removed from the cache if the cache is already at its maximal capacity. Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value. 

We'll also need a `get` operation that fetches a value given a key. When a key-value pair is fetched from the cache, we'll go through the same priority-increase dance that also happens when a new pair is added to the cache.

Note that the only way for entries to be removed from the cache is when one needs to be evicted to make room for a new one. Thus, there is no explicit `remove` method. 

Given the above spec, try to get a working implementation that passes the tests. What data structure(s) might be good candidates with which to build our cache on top of? Hint: Since our cache is going to be storing key-value pairs, we might want to use a structure that is adept at handling those. 

---

Once you've gotten the tests passing, it's time to analyze the runtime complexity of your `get` and `set` operations. There's a way to get both operations down to sub-linear time. In fact, we can get them each down to constant time by picking the right data structures to use. 

Here are you some things to think about with regards to optimizing your implementation: If you opted to use a dictionary to work with key-value pairs, we know that dictionaries give us constant access time, which is great. It's cheap and efficient to fetch pairs. A problem arises though from the fact that dictionaries don't have any way of remembering the order in which key-value pairs are added. But we definitely need something to remember the order in which pairs are added. Can you think of some ways to get around this constaint?
