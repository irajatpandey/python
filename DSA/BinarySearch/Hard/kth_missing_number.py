# kth_missing_number.py - Kth missing positive number

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # Note: Removing 'self' for simplicity if not running within a class instance.
        # start, end = 0, len(arr) - 1 
        start, end = 0, len(arr) - 1

        # 'start' will eventually point to the position *after* the last element 
        # whose Missing Count is < K.
        while start <= end:
            mid = start + (end - start) // 2
            
            # Calculate how many numbers are missing before arr[mid].
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                # Case 1: Not enough missing numbers found yet.
                # The Kth missing number must be further right.
                start = mid + 1  # Search right
            else:
                # Case 2: Kth missing number is at or before this point.
                # Try to find a smaller index (go left).
                end = mid - 1    # Search left
        
        # Loop termination par, 'start' (jo ab 'end + 1' hai) woh index hai jahan:
        # arr[start-1] tak ka missing count < K hai.
        
        # Missing numbers till arr[start-1]:
        missing_till_end = arr[start - 1] - (start - 1 + 1) if start > 0 else 0
        
        # Remaining missing numbers needed: k - missing_till_end
        
        # The Kth missing number is:
        # Last available number + remaining needed
        # = arr[start - 1] + (k - missing_till_end)
        
        # Simplified Formula: K + start 
        # (This is derived from substituting the Missing Count formula)
        
        return k + start

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 4, 7, 11], 5, 9),
        ([1, 2, 3, 4], 2, 6), # Missing are 5, 6... 2nd is 6
        ([1, 3, 4], 1, 2)
    ]
    
    for arr, k, expected in test_cases:
        result = find_kth_missing(arr, k)
        print(f"Array: {arr}, K={k}: Expected={expected}, Got={result}")