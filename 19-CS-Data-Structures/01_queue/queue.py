class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        item = self.storage.pop_head() # popping from head is easier than tail
        if item:
            self.size -= 1
        return item

    def len(self):
        return self.size


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

    def __repr__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # methods to add to list
    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head:  # so we can first add to head/tail
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head:  # so we can first add to head/tail
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

    # method to remove from list
    def pop_head(self):
        if not self.head:
            return None
        else:
            temp_node = self.head
            self.head = self.head.get_next()
            return temp_node.value
