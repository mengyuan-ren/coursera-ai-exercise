import unittest
from translator import english_to_french, french_to_english

class Test(unittest.TestCase):
    def test_eng_french(self):
        self.assertEqual(
            english_to_french("good"), 
            "Bon"
        )
        self.assertNotEqual(english_to_french(
            "good"), 
            "Good"
        )
        self.assertEqual(english_to_french(
            None), 
            ""
        )

    def test_french_eng(self):
        self.assertEqual(
            french_to_english("bon"), 
            "Good"
        )
        self.assertNotEqual(
            french_to_english("bon"), 
            "Bon"
        )
        self.assertEqual(french_to_english(
            None), 
            ""
        )

unittest.main()
