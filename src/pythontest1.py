import unittest

def is_even(nbr):
    """
    Cette fonction teste si un nombre est pair.
    """
    return nbr % 2 == 0

class MyTest(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(6))
        self.assertFalse(is_even(1))
        self.assertEqual(is_even(0), True)
    def test_lstrip(self): #testing for left stripping
        self.assertEqual('   hello '.lstrip(),'hello ')
    def test_isupper(self): #testing for isupper
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('HELlO'.isupper())

if __name__ == '__main__':
    unittest.main()
