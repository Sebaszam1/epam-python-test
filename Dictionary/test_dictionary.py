import unittest
from dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    
    def setUp(self):
        self.dictionary = Dictionary()

    def test_add_word_new(self):
        self.dictionary.add_word("Colombia", "Country")
        self.assertIn("Colombia", self.dictionary.words)
        self.assertEqual(self.dictionary.words["Colombia"], ["Country"])

    def test_get_definitions_existing_word(self):
        self.dictionary.add_word("Colombia", "Country")
        self.assertEqual(self.dictionary.get_definitions("Colombia"), ["Country"])

    def test_get_definitions_non_existing_word(self):
        self.assertEqual(self.dictionary.get_definitions("Canada"), "The word 'Canada' does not exist.")

    def test_list_words(self):
        self.dictionary.add_word("Colombia", "Beautiful country")
        self.dictionary.add_word("Canada", "Great country")
        self.assertEqual(set(self.dictionary.list_words()), {"Colombia", "Canada"})

    def test_list_words_empty(self):
        self.assertEqual(self.dictionary.list_words(), [])

if __name__ == '__main__':
    unittest.main()
