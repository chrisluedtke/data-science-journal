class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage)-1)

    def delete(self):
        if not self.storage:
            return None
        elif len(self.storage) == 1:
            return self.storage.pop()
        else:
            top = self.storage[0]  # store top heap value so we can return it
            self.storage[0] = self.storage.pop()
            self._sift_down(0)
            return top

    def get_max(self):
        if self.storage:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            # compare to parent
            parent = (index - 1) // 2  # floor division

            if parent < 0:
                break

            if self.storage[parent] < self.storage[index]:
                self.storage[index], self.storage[parent] = \
                    self.storage[parent], self.storage[index]  # swap

                index = parent
            else:
                break

    def _sift_down(self, index):
        end_i = len(self.storage) - 1
        l_i = 2 * index + 1

        while l_i <= end_i:
            r_i = l_i + 1

            if (r_i <= end_i and self.storage[l_i] < self.storage[r_i]):
                swap_i = r_i
            else:
                swap_i = l_i

            if self.storage[index] < self.storage[swap_i]:
                self.storage[index], self.storage[swap_i] = \
                    self.storage[swap_i], self.storage[index]  # swap

                index = swap_i
                l_i = 2 * index + 1
            else:
                break
