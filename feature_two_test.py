import copy
import unittest
import random

import multi_dimension_sort


class multi_sort_test(unittest.TestCase):
    def test_multi_sort(self):
        arraySolution = [[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]]
        iterations = 10

        while iterations > 0:
            newArray = copy.deepcopy(arraySolution)

            random.shuffle(newArray)
            print(newArray)
            for array in newArray:
                print(array)
                random.shuffle(array)
                print(array)
            print(newArray)
            sortedArray = multi_dimension_sort.multi_sort(newArray)
            self.assertEqual(arraySolution, sortedArray)  # add assertion here
            iterations -= 1


if __name__ == '__main__':
    unittest.main()
