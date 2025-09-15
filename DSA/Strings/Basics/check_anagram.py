def are_anagrams(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    """
    pass

if __name__ == "__main__":
    s1, s2 = "listen", "silent"
    s3, s4 = "hello", "world"
    print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")
    print(f"Are '{s3}' and '{s4}' anagrams? {are_anagrams(s3, s4)}")