from doubly_linked_list import DoublyLinkedList


class TextBuffer:
    def __init__(self, init=None):
        # check if an init string is provided
        # if so, put the contents of the init string in self.contents
        self.contents = DoublyLinkedList()

        if init:
            self.append(init)

    def __str__(self):
        # needs to return a string to print
        s = ""
        current = self.contents.head
        while current:
            s += current.value
            current = current.next
        return s

    def append(self, string_to_add):
        for char in string_to_add:
            self.contents.add_to_tail(char)

    def prepend(self, string_to_add):
        # reverse the incoming string ot maintain correct
        # order when adding to the front of the text buffer
        for char in string_to_add[::-1]:
            self.contents.add_to_head(char)

    def delete_front(self, chars_to_remove: int):
        for _ in range(chars_to_remove):
            self.contents.remove_from_head()

    def delete_back(self, chars_to_remove: int):
        for _ in range(chars_to_remove):
            self.contents.remove_from_tail()

    def join(self, other_buffer):
        """Join other_buffer to self
        The input buffer gets concatenated to the end of this buffer
        The tail of the concatenated buffer will be the tail of the other buffer
        The head of the concatenated buffer will be the head of this buffer
        """
        if not isinstance(other_buffer, TextBuffer):
            raise Exception('Error: Atgument is not a text buffer')
        elif other_buffer.contents.length == 0:
            raise Exception('Error: Other buffer is empty')

        self.contents.tail.next = other_buffer.contents.head
        other_buffer.contents.head.prev = self.contents.tail
        self.contents.tail = other_buffer.contents.tail
        self.contents.length += other_buffer.contents.length


if __name__ in "__main__":
    text = TextBuffer("Super")
    print(text)

    text.append("asdfasdflkajsfd")
    print(text)

    text.append(" is ")
    text.join(TextBuffer("weird."))

    print(text)

    text.delete_back(6)
    print(text)

    text.prepend("Hey!")
    print(text)
