import unittest
from reverse_words import rev_string


class TestReverse(unittest.TestCase):
    def test_rev_string(self):
        self.assertEqual("I evol gnimmargorp", rev_string("I love programming"))
        self.assertEqual("Please give me good input", rev_string("      "))
        self.assertEqual("Please give me good input", rev_string(""))
        self.assertEqual("oof rab zab", rev_string("foo bar baz"))
        self.assertEqual("oof i zab", rev_string("foo i baz"))


if __name__ == '__main__':
    unittest.main()
