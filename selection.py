#!/usr/bin/env python
# encoding: utf-8
import unittest


def selection_sort(array):
    l = len(array)
    for i in xrange(l):
        min = i
        for j in xrange(i, l):
            if array[j] < min:
                min = j
        array[min], array[i] = array[i], array[min]
    return array


class SelectionCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_selection(self):
        empty_array = []
        self.assertEqual(selection_sort(empty_array), [])

        sorted_array = [1, 2, 3]
        self.assertEqual(selection_sort(sorted_array), [1, 2, 3])

        unsorted_array = [-1, 2, 0, -3]
        self.assertEqual(selection_sort(unsorted_array), [-3, -1, 0, 2])


if __name__ == '__main__':
    unittest.main()
