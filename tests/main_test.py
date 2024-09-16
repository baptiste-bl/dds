import unittest
from DonneDesSous.main import donne_des_sous, compte_en_banque


class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = donne_des_sous(12, 10)
        self.assertEqual(compte_en_banque, 24)

    def test_something_else(self):
        compte_en_banque = donne_des_sous(9, 10)
        self.assertEqual(compte_en_banque, 19)
if __name__ == '__main__':
    unittest.main()
