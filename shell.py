#!/usr/bin/env python
# encoding: utf-8
import unittest


def shell_sort(array):
    n = len(array)
    gap = int(round(n / 2.0))
    while gap > 0:
        for i in xrange(gap, n):
            temp = array[i]
            j = i
            while j >= gap and temp < array[j - gap]:
                array[j] = array[j - gap]
                j = j - gap
            array[j] = temp
        gap = int(round((gap - 1) / 2.0))
    return array


class ShellCase(unittest.TestCase):
    def setUp(self):
        pass

    def teartDown(self):
        pass

    def test_shell_sort(self):
        empty_array = []
        self.assertEqual([], shell_sort(empty_array))

        unsorted_array = [0, -1, 1, -3]
        self.assertEqual([-3, -1, 0, 1], shell_sort(unsorted_array))

        sorted_array = [-3, -1, 0, 1]
        self.assertEqual([-3, -1, 0, 1], shell_sort(sorted_array))


if __name__ == '__main__':
    unittest.main()
