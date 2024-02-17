import sys
import os

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from bubble_sort import sort_arguments_or_config

class TestBubbleSort(unittest.TestCase):
    def test_sort_numeric_values(self):
        # Test sorting numeric values
        unsorted_array = [4, 2, 7, 1, 5]
        expected_sorted_array = [1, 2, 4, 5, 7]
        self.assertEqual(sort_arguments_or_config(*unsorted_array), expected_sorted_array)

    def test_sort_alphanumeric_values(self):
        # Test sorting alphanumeric values
        unsorted_array = ['c', 'a', 'b', '1', '3', '2']
        expected_sorted_array = ['1', '2', '3', 'a', 'b', 'c']
        self.assertEqual(sort_arguments_or_config(*unsorted_array), expected_sorted_array)

    def test_sort_with_config(self):
        # Test sorting with default list from config
        expected_sorted_array = [1, 1, 1.01, 6, 12, 23, 23, 45, 65, 91, 154]
        self.assertEqual(sort_arguments_or_config(), expected_sorted_array)

if __name__ == '__main__':
    unittest.main()
