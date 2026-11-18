import unittest
from decimal import Decimal
from validatie import valideer_bedrag


class TestValidatieBedrag(unittest.TestCase):

    def test_geldig_bedrag(self):
        self.assertEqual(valideer_bedrag("50"), Decimal("50"))

    def test_decimaal_bedrag(self):
        self.assertEqual(valideer_bedrag("25.50"), Decimal("25.50"))

    def test_nul_bedrag(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("0")

    def test_negatief_bedrag(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("-10")

    def test_ongeldige_invoer(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("abc")

    def test_lege_invoer(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("")

    def test_nan(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("NaN")

    def test_oneindig(self):
        with self.assertRaises(ValueError):
            valideer_bedrag("Infinity")


if __name__ == "__main__":
    unittest.main()