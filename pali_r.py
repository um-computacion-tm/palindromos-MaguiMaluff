import unittest


def palindrome(word):
    if len(word) <= 1:
        return True
    pal = word.lower()
    if pal[0] == pal[-1]:
        return palindrome(word[1:-1])
    else:
        return False

if __name__ == '__main__':
    unittest.main()