def reverse_words(s: str) -> str:
    """
    Reverses the order of words in a given string.
    """
    pass

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    pass

if __name__ == "__main__":
    # Example for reversing words
    s1 = "hello world"
    reversed_s1 = reverse_words(s1)
    print(f"Original: '{s1}' -> Reversed: '{reversed_s1}'")

    # Example for palindrome check
    s2 = "racecar"
    s3 = "hello"
    print(f"Is '{s2}' a palindrome? {is_palindrome(s2)}")
    print(f"Is '{s3}' a palindrome? {is_palindrome(s3)}")