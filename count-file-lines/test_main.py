import unittest
from main import *

class TestCountFileLines(unittest.TestCase):
    def test_file_line_count(self):
        self.assertEqual(line_count(filename='README.md', lookup_value=''), 77)

    def test_file_line_count_with_optional_argument(self):
        self.assertEqual(line_count(filename='README.md', lookup_value='Validation'), 2)
        self.assertEqual(line_count(filename='README.md', lookup_value='Testing'), 1)
        self.assertEqual(line_count(filename='README.md', lookup_value='-1'), 0)

    def test_file_line_count_wrong_file(self):
        self.assertEqual(line_count(filename='dummy.txt', lookup_value='Flow'), -1)


if __name__ == "__main__":
    unittest.main()
