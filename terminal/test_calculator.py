import unittest
import re


class TestAcademicPortal(unittest.TestCase):
    def setUp(self):
        self.email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
        self.name_regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ]{2,}$"

    def test_valid_email(self):
        self.assertTrue(re.match(self.email_regex, "student@school.com"))
        self.assertTrue(re.match(self.email_regex, "matheus.dias@domain.com.br"))

    def test_invalid_email(self):
        self.assertFalse(re.match(self.email_regex, "asd"))
        self.assertFalse(re.match(self.email_regex, "student@school"))

    def test_valid_name(self):
        self.assertTrue(re.match(self.name_regex, "Matheus"))

    def test_invalid_name(self):
        self.assertFalse(re.match(self.name_regex, "M"))
        self.assertFalse(re.match(self.name_regex, "Matheus123"))


if __name__ == "__main__":
    unittest.main()