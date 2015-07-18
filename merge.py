#!/usr/bin/env python
# encoding: utf-8
import unittest


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    mid = int(n / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


class MergeClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge_sort(self):
        empty_array = []
        self.assertEqual(empty_array, merge_sort(empty_array))

        unsorted_array = [0, -1, 1, -3]
        self.assertEqual([-3, -1, 0, 1], merge_sort(unsorted_array))

        sorted_array = [-3, -1, 0, 1]
        self.assertEqual([-3, -1, 0, 1], merge_sort(sorted_array))


if __name__ == '__main__':
    unittest.main()
