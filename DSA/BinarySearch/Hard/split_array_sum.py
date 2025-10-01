from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum possible value of the maximum sum among K contiguous subarrays 
        using Binary Search on the Answer.
        
        Args:
            nums (List[int]): The array of numbers to be split.
            k (int): The number of required subarrays (splits).

        Returns:
            int: The minimum achievable maximum subarray sum.
        """
        
        # --- 1. Edge Case Check ---
        # If the number of subarrays (k) is greater than the number of elements (N), 
        # it's an impossible split or results in single-element subarrays. 
        # Since the problem implies non-empty subarrays, if k > N, it's impossible.
        if k > len(nums):
            return -1 # Or handle as per specific platform constraint
        
        def check(nums: List[int], k: int, max_sum_limit: int) -> bool:
            """
            Feasibility function: Checks if the array can be split into K or fewer 
            subarrays such that no subarray sum exceeds 'max_sum_limit'.
            """
            subarrays_needed = 1  # Start with the first subarray
            current_sum = 0
            
            for num in nums:
                # If adding the current number exceeds the max sum limit
                if current_sum + num > max_sum_limit:
                    # Start a new subarray
                    subarrays_needed += 1
                    current_sum = num  # New subarray starts with the current number
                else:
                    # Add number to the current subarray
                    current_sum += num
            
            # The split is possible if the required subarrays are within the limit k.
            return subarrays_needed <= k

        # --- 2. Define Search Space ---
        # Start (Lower Bound): The smallest possible max sum is the largest single element.
        start = max(nums) 
        # End (Upper Bound): The largest possible max sum is the total sum of all elements.
        end = sum(nums)
        
        # 'ans' stores the smallest valid max_sum_limit found so far.
        ans = -1 
        
        # --- 3. Binary Search Execution ---
        while start <= end:
            mid = start + (end - start) // 2  # The current potential max sum limit
            
            # Check feasibility with the current limit (mid)
            if check(nums, k, mid):
                # Feasible! Store it and try to find an even smaller limit (search left).
                ans = mid
                end = mid - 1
            else:
                # Not feasible. The limit (mid) is too small. Increase the limit (search right).
                start = mid + 1
                
        # 'ans' holds the minimum largest sum required.
        return ans

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        # (nums, k, expected_min_max_sum)
        ([7, 2, 5, 10, 8], 2, 18),  # Split: [7, 2, 5] (14) | [10, 8] (18). Max is 18.
        ([1, 2, 3, 4, 5], 2, 9),    # Split: [1, 2, 3] (6) | [4, 5] (9). Max is 9.
        ([1, 4, 4], 3, 4),          # Split: [1], [4], [4]. Max is 4.
        ([10, 5, 13, 4, 7, 9, 10], 4, 17), 
        ([1, 2, 3], 4, -1)           # Edge Case: k > N
    ]
    
    print("--- Split Array Largest Sum Test Results ---")
    for nums, k, expected in test_cases:
        result = s.splitArray(nums, k)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Array: {nums}, Splits: {k}")
        print(f"  Expected Min Max Sum: {expected}, Got: {result} ({status})")
    print("-" * 50)