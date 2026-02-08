import unittest
from data import languages, operators, operator_languages
from logic import *

class TestOperatorLogic(unittest.TestCase):

    def test_languages_with_c(self):
        result = get_languages_with_c(languages, operators)
        self.assertIn("C++", result)
        self.assertEqual(result["C++"], ["Борис", "Алина"])

    def test_average_salary(self):
        result = get_average_salary_by_language(languages, operators)
        self.assertEqual(result["Python"], 80000.0)

    def test_operators_starting_with_a(self):
        result = get_operators_starting_with_a(
            operators, languages, operator_languages
        )
        self.assertIn("Алиса", result)
        self.assertIn("Python", result["Алиса"])


if __name__ == "__main__":
    unittest.main()