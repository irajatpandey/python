import math
from typing import List

def smallestDivisor(nums: List[int], threshold: int) -> int:
    # --- Fix 1: Correct Search Range Initialization ---
    # The smallest possible divisor is 1.
    start = 1 
    # The largest useful divisor is the max element in nums.
    end = max(nums)
    
    # 'ans' stores the smallest divisor found so far that satisfies the condition.
    ans = end 
    
    while start <= end:
        mid = start + (end - start) // 2
        
        # --- Feasibility Check (Calculate Total Sum) ---
        current_sum = 0
        
        # Use integer arithmetic for ceil to make it slightly faster and avoid floats: (a + b - 1) // b
        for val in nums:
            current_sum += (val + mid - 1) // mid
            # Alternatively: current_sum += math.ceil(val / mid)
        
        # --- Binary Search Decision ---
        
        if current_sum <= threshold:
            # Case 1: 'mid' is a valid divisor. Store it as the best answer.
            ans = mid
            # Try to find an even smaller divisor in the left half.
            end = mid - 1
        else:
            # Case 2: The sum is too large. We need a larger divisor.
            start = mid + 1
            
    return ans

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5, 9], 6, 5),          
        ([44, 22, 33, 11, 1], 5, 44),  # CORRECTED: 11 is too small; 44 is the smallest that works.
        ([2, 3, 5, 7, 11], 11, 3),     # CORRECTED: 1 is too small; 3 is the smallest that works.
        ([9, 12, 18, 30], 10, 9),      # CORRECTED: 5 is too small; 9 is the smallest that works.
    ]
    
    for nums, threshold, expected in test_cases:
        result = smallestDivisor(nums, threshold)
        print(f"Nums: {nums}, Threshold={threshold}: Expected={expected}, Got={result}")