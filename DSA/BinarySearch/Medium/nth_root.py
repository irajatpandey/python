# nth_root.py - Find the Nth root of a number using binary search
import math
def find_nth_root(n: int, m: int) -> float:
    """
    Stub function to find the Nth root of number M using binary search.
    (Solution logic goes here)
    """
    # Example: If n=3 (cube root) and m=27, the result should be 3.
    # Returns a float for precision, but often an integer if exact root is required.

    if n == 1:
        return 1.0
    
    start = 1
    end = m
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2 
        if pow(mid, n) == m:
            return float(mid)

        elif mid ** n > m:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans

if __name__ == "__main__":
    test_cases = [
        (3, 27, 3.0),
        (2, 49, 7.0),
        (4, 81, 3.0),
        (3, 29, 3.036) # Approx value for cube root of 29
    ]
    
    for n, m, expected_approx in test_cases:
        result = find_nth_root(n, m)
        # Note: In a real test, you'd compare result with expected within a tolerance.
        print(f"{n}th root of {m}: Expected Approx={expected_approx}, Got={result}")