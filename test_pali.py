import unittest
from pali_i import palindrome
from pali_r import palindrome

class PaliTest(unittest.TestCase):
    def test_1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)
    def test_2(self):
        result = palindrome('NeuQuEn')
        self.assertEqual(result, True)
    def test_3(self):
        result = palindrome('hola')
        self.assertEqual(result, False)
    def test_4(self):
        result = palindrome('mundo')
        self.assertEqual(result, False)
    def test_5(self):
        result = palindrome('aabcaa')
        self.assertEqual(result, False)
    def test_6(self):
        result = palindrome('abccba')
        self.assertEqual(result, True)
    def test_7(self):
        result = palindrome('baac')
        self.assertEqual(result, False)
    def test_8(self):
        result = palindrome('caad')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()