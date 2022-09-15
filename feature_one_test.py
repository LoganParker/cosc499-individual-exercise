import random
import unittest

import single_dimension_sort


class featureOneTest(unittest.TestCase):
    def test_sort(self):
        testcases = [[], [], [], [], []]
        for array in testcases:
            arraylength = random.randint(0, 999)
            while len(array) < arraylength:
                array.append(random.randint(-1000, 1000))
            programTested = single_dimension_sort.single_sort()
            pySorted = array.sort()
            self.assertEqual(pySorted, programTested)  # add assertion here


if __name__ == '__main__':
    unittest.main()
