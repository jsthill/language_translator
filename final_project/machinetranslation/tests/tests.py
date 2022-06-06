import unittest
from machinetranslation import translator
from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def text1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Man'), 'Homme')
        self.assertIsNone(english_to_french(''), '')

class TestFrenchToEnglish(unittest.TestCase):
    def text1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Homme'), 'Man')
        self.assertIsNone(french_to_english(''), '')

if __name__ == '__main__':
    unittest.main()
