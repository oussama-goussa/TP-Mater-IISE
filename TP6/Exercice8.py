#Exercice8.py

import unittest

from Exercice6 import safe_division

class TesterProcessInput(unittest.TestCase):
    
    def tester_valueError(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(5,0)
        
        result = safe_division(5,1)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
