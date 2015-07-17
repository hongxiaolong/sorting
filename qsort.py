#!/usr/bin/env python
# encoding: utf-8
import unittest


def quick_sort(array):
    return qsort(array, 0, len(array) - 1)


def qsort(array, left, right):
    if left >= right:
        return array
    key = array[left]
    l, r = left, right
    while l < r:
        # 必须让r先走，当r <= l时l不会再走，否则会导致l多走一步
        while key <= array[r] and r > l:
            r -= 1
        while key >= array[l] and l < r:
            l += 1
        array[l], array[r] = array[r], array[l]
    array[left], array[l] = array[l], array[left]
    qsort(array, left, l - 1)
    qsort(array, r + 1, right)
    return array


class QuichCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_quick_sort(self):
        empty_array = []
        self.assertEqual([], quick_sort(empty_array))

        unsorted_array = [-1, 0, 1, -3]
        self.assertEqual([-3, -1, 0, 1], quick_sort(unsorted_array))

        sorted_array = [-3, -1, 0, 1]
        self.assertEqual([-3, -1, 0, 1], quick_sort(sorted_array))


if __name__ == '__main__':
    unittest.main()
