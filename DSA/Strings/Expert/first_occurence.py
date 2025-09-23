def find_first_occurrence(haystack: str, needle: str) -> int:
    j = 0
    for i in range(len(haystack) - len(needle) + 1):
        j = 0
        while j < len(needle):
            if haystack[i + j] == needle[j]:
                j += 1
            else:
                break
        if j == len(needle):
            return i
    return -1

def run_tests():
    test_cases = [
        # Test Case 1: Simple match
        ("hello", "ll", 2),
        
        # Test Case 2: No match
        ("aaaaa", "bba", -1),
        
        # Test Case 3: Match at the beginning
        ("sadbutsad", "sad", 0),
        
        # Test Case 4: Needle is empty
        ("leetcode", "", 0),
        
        # Test Case 5: Needle is longer than haystack
        ("abc", "abcdef", -1),
        
        # Test Case 6: Match at the end
        ("mississippi", "pi", 9),
        
        # Test Case 7: Same string
        ("abc", "abc", 0),
    ]

    for haystack, needle, expected in test_cases:
        result = find_first_occurrence(haystack, needle)
        print(f"Haystack: '{haystack}', Needle: '{needle}'")
        print(f"Expected: {expected}, Got: {result}")
        
        if result == expected:
            print("✅ Test Passed!")
        else:
            print("❌ Test Failed!")
        print("-" * 20)

# Uncomment to run the tests
run_tests()