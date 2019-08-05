class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTreeNode(value)  
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTreeNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        elif (target < self.value) and self.left:
            return self.left.contains(target)
        elif (self.value < target) and self.right:
            return self.right.contains(target)
        else:
            return False

    def get_max(self):
        if not self.value:
            return None
        elif self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
