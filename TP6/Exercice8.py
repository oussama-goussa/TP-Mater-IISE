#Exercice8.py

import unittest

from Exercice6 import safe_division
from Exercice4 import set_age, NegativeAgeError
from Exercice2 import convert_to_int

class TesterProcessInput(unittest.TestCase):
    
    def test_convert_to_int(self):
        with self.assertRaises(ValueError):
            convert_to_int("abc")

        result = convert_to_int("42")
        self.assertEqual(result, 42)

    def test_set_age(self):
        with self.assertRaises(NegativeAgeError):
            set_age(-7)

        result = set_age(5)
        self.assertEqual(result, None)

    def tester_safe_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(5,0)
        
        result = safe_division(5,1)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
