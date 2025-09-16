def are_anagrams(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other.
    """
    cache = {}
    for char in s1:
        cache[char] = cache.get(char, 0) + 1
    
    for char in s2:
        if char in cache:
            cache[char] -= 1
        else:
            return False
    
    for count in cache.values():
        if count != 0:
            return False
    return True
    


if __name__ == "__main__":
    s1, s2 = "listen", "silent"
    s3, s4 = "hello", "world"
    print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")
    print(f"Are '{s3}' and '{s4}' anagrams? {are_anagrams(s3, s4)}")