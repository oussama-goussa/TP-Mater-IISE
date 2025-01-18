#Exercice8.py

import unittest

from Exercice5 import process_input

class TesterProcessInput(unittest.TestCase):
    def tester_division_succes(self):
        self.assertEqual(process_input("100"), "Le résultat de la division est : 10.0")

    def tester_valueError(self):
        self.assertEqual(process_input("abc"), "Veuillez entrer un nombre entier valide.")

if __name__ == '__main__':
    unittest.main()
