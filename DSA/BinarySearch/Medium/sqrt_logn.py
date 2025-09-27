# sqrt_logn.py - Find square root of a number in O(log n)

def find_sqrt(n: int) -> int:
    """
    Stub function to find the integer square root of n using binary search.
    (Solution logic goes here)
    """
    # Example: If n=16, the result should be 4 (or 4.0 if floating point).
    # Return type is often integer for competitive programming problems.
    return 0 

if __name__ == "__main__":
    test_cases = [
        (4, 2),
        (8, 2),  # Floor of sqrt(8) is 2
        (16, 4),
        (0, 0),
        (120, 10) # Floor of sqrt(120) is 10
    ]
    
    for number, expected in test_cases:
        result = find_sqrt(number)
        print(f"sqrt({number}): Expected={expected}, Got={result}")