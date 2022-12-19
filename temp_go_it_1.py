def is_palindrome(word):
    return True if word[::-1] == word else False
print(is_palindrome("abba"))