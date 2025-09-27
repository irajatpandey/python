# sqrt_logn.py - Find square root of a number in O(log n)

def find_sqrt(n: int) -> int:
    """
    Stub function to find the integer square root of n using binary search.
    This function finds the largest integer x such that x*x <= n.
    """
    
    # --- Edge Case Handling ---
    # Handle the simplest cases: sqrt(0) is 0, sqrt(1) is 1.
    # Note: If n=0 is allowed, you should handle it (or let the loop handle it, 
    # but the logic already covers it as start=1 won't execute the loop).
    if n == 0: 
        return 0
    if n == 1: 
        return 1
        
    # --- Binary Search Initialization ---
    start = 1
    end = n             # Search space starts from 1 up to n.
    ans = 0             # 'ans' will store the best possible floor value found so far.
    
    while start <= end:
    
        mid = start + (end - start) // 2
        
        # --- Core Comparison Logic ---
        
        # Case 1: Perfect Square Found
        if mid * mid == n:
            return mid
            
        # Case 2: mid*mid is too large
        elif (mid * mid) > n:
            # The answer must be in the left half.
            end = mid - 1
            
        # Case 3: mid*mid is less than n (Potential Answer)
        else:
            # 'mid' is a potential floor value (mid*mid <= n). Store it.
            ans = mid
            # Try to find a better (larger) floor value in the right half.
            start = mid + 1
            
    # If a perfect square wasn't found, 'ans' holds the largest integer 'mid'
    # such that mid*mid <= n (the floor of the square root).
    return ans
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