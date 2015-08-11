#!/usr/bin/env python
# encoding: utf-8
import unittest


def heap_sort(array):
    n = len(array)
    last_non_leaf = int(n / 2 - 1)
    for i in xrange(last_non_leaf, -1, -1):
        max_heap(array, i, n - 1)
    for max in xrange(n - 1, 0, -1):
        array[0], array[max] = array[max], array[0]
        max_heap(array, 0, max - 1)
    return array


def max_heap(array, start, end):
    if start >= end:
        return array
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child = child + 1
        if array[child] > array[root]:
            array[child], array[root] = array[root], array[child]
            root = child
        else:
            break


class HeapCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_heap_sort(self):
        empty_array = []
        self.assertEqual([], heap_sort(empty_array))

        unsorted_array = [-1, 0, 1, 1, -3]
        self.assertEqual([-3, -1, 0, 1, 1], heap_sort(unsorted_array))

        sorted_array = [-3, -1, 0, 1, 1]
        self.assertEqual([-3, -1, 0, 1, 1], heap_sort(sorted_array))


if __name__ == '__main__':
    unittest.main()
