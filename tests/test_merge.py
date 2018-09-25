import unittest

from pacyam.pacyam import merge_dicts


class MergeDictTestCase(unittest.TestCase):

    def test_merge_basic(self):
        a = {'a': 1, 'b': 2}
        b = {'c': 2}

        expected = {'a': 1, 'b': 2, 'c': 2}

        result = merge_dicts(a, b)
        self.assertEqual(expected, result)

    def test_merge_overwrite(self):
        a = {'a': 1, 'b': 2}
        b = {'b': 5}

        expected = {'a': 1, 'b': 5}

        result = merge_dicts(b, a)  # Destination takes precedence
        self.assertEqual(expected, result)

    def test_merge_list(self):
        a = {'a': [1, 2, 3]}
        b = {'a': [4, 5]}

        expected = {'a': [1, 2, 3, 4, 5]}

        result = merge_dicts(b, a)
        self.assertEqual(expected, result)

    def test_merge_deep(self):
        a = {
            'a': {
                'd': [1, 2]
            }
        }
        b = {
            'a': {
                'c': 5,
                'd': [3, 4]
            }
        }

        expected = {
            'a': {
                'c': 5,
                'd': [3, 4, 1, 2]
            }
        }

        result = merge_dicts(a, b)
        self.assertEqual(expected, result)
