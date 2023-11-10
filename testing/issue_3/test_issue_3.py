import unittest

from issue_3 import fit_transform

expected = [
    ("apple", [0, 0, 1]),
    ("banana", [0, 1, 0]),
    ("apple", [0, 0, 1]),
    ("cherry", [1, 0, 0]),
]


class TestFitTransform(unittest.TestCase):
    def test_list_input(self):
        result = fit_transform(["apple", "banana", "apple", "cherry"])
        self.assertEqual(result, expected)

    def test_strs_input(self):
        result = fit_transform("apple", "banana", "apple", "cherry")
        self.assertEqual(result, expected)

    def test_no_arguments_raises(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_repeated_categories(self):
        result = fit_transform("apple", "banana", "apple", "cherry")
        self.assertIn(("banana", [0, 1, 0]), result)
        self.assertEqual(len(result), 4)


if __name__ == "__main__":
    unittest.main()
