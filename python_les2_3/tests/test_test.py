'''

In this file I just try to creat some test.

'''

import unittest


def my_sort(lst):
    was_swaped = True
    while was_swaped:
        was_swaped = False
        for i in range(len(lst)-1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                was_swaped = True
    return lst


class MyFirstTest(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(my_sort([4, 2, 5, 1, 3]), [5, 4, 3, 2, 1])

    def test_2(self):
        self.assertAlmostEqual(my_sort([]), [])

    def test_4(self):
        self.assertAlmostEqual(my_sort([-1]), [-1])


if __name__ == '__main__':
    unittest.main()
