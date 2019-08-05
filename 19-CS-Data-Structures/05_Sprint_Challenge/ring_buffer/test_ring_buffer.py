import unittest
from ring_buffer import RingBuffer

class RingBufferTests(unittest.TestCase):
    def setUp(self):
        self.buffer = RingBuffer(5)

    def test_ring_buffer(self):
        self.assertEqual(len(self.buffer.storage), 5)

        self.buffer.append('a')
        self.buffer.append('b')
        self.buffer.append('c')
        self.buffer.append('d')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd'])

        self.buffer.append('e')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['a', 'b', 'c', 'd', 'e'])

        self.buffer.append('f')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['f', 'b', 'c', 'd', 'e'])

        self.buffer.append('g')
        self.buffer.append('h')
        self.buffer.append('i')
        self.assertEqual(len(self.buffer.storage), 5)
        self.assertEqual(self.buffer.get(), ['f', 'g', 'h', 'i', 'e'])


if __name__ == '__main__':
    unittest.main()