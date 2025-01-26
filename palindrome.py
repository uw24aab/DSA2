def is_palindrome(word: str) -> bool:
    # base case: if the length of the word is 0 or 1, it's a palindrome
    if len(word) <= 1:
        return True
    # recursive case: check if first and last characters are same.
    if word[0] == word[-1]:
        return is_palindrome(
            word[1:-1]
        )  # then check the substring excluding the first and last characters.
    # if first and last characters don't match word is not a palindrome.
    return False


print(is_palindrome("gag"))  # True
print(is_palindrome("pop"))  # True
print(is_palindrome("hannah"))  # True
print(is_palindrome("rotator"))  # True
print(is_palindrome("hello"))  # False
