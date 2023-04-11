import unittest

def palindrome(word):
    pal = word.lower()
    for i in range(len(word) + 1):
        if pal[0] == pal[-1]:
            word = word[1 : -1]
            return True
        else:
            return False
        
if __name__ == '__main__':
    unittest.main()