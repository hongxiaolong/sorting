#!/usr/bin/env python
# encoding: utf-8
import unittest


def insertion_sort(array):
    l = len(array)
    for i in xrange(1, l):
        value = array[i]
        index = i
        for j in xrange(i - 1, -1, -1):
            if value < array[j]:
                array[j + 1] = array[j]
                index = j
                continue
            break
        array[index] = value
    return array


class InsertionSortCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_insertion_sort(self):
        empty_array = []
        self.assertEqual([], insertion_sort(empty_array))

        unsorted_array = [5, 2, 4, -1, 0]
        self.assertEqual([-1, 0, 2, 4, 5], insertion_sort(unsorted_array))

        sorted_array = [-1, 0, 2, 4, 5]
        self.assertEqual([-1, 0, 2, 4, 5], insertion_sort(sorted_array))


if __name__ == "__main__":
    unittest.main()
