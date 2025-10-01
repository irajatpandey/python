from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a Rotated Sorted Array that contains duplicates.
        (Solution logic goes here, including handling the nums[start] == nums[mid] case)
        """
        start = 0
        end = len(nums) - 1
        current_min = nums[0] 

        while start <= end:
            # Check 1: Agar segment already sorted hai, toh nums[start] minimum hai.
            # Use <= to handle cases where all elements are equal (e.g., [1, 1, 1]).
            if nums[start] < nums[end]:
                current_min = min(current_min, nums[start])
                break 
            
            mid = start + (end - start) // 2
            
            # Check 2: current_min ko update karo with nums[mid]
            current_min = min(current_min, nums[mid])

            # Check 3: Handle Duplicates (The necessary step for Problem 154)
            if nums[start] == nums[mid]:
                # Ambiguity: Minimum left ya right mein ho sakta hai.
                # Safe move: Duplicate element ko discard karke aage badho.
                start += 1
                continue 
            
            # Check 4: Pointer Movement Logic
            
            # Left half is sorted:
            if nums[start] <= nums[mid]:
                # Minimum right (unsorted) half mein hoga.
                start = mid + 1
            
            # Right half is sorted:
            else: 
                # Minimum left (unsorted) half mein hoga.
                end = mid - 1
                
        return current_min

# --- Driver Function and Test Cases ---
def run_tests():
    s = Solution()
    test_cases = [
        ([1, 3, 5], 1),          # No rotation, no duplicates
        ([2, 2, 2, 0, 1], 0),    # Duplicates forcing start++
        ([3, 1, 3], 1),          # Tricky duplicate case
        ([10, 1, 10, 10, 10], 1), # Duplicates around the pivot
        ([1, 1, 1, 1], 1),       # All duplicates
        ([4, 5, 6, 7, 0, 1, 2], 0), # Simple rotation (Problem 153 case)
    ]

    print("--- Find Minimum in Rotated Sorted Array II ---")
    for nums, expected in test_cases:
        result = s.findMin(nums)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        
        print(f"Array: {nums}")
        print(f"Expected Min: {expected}, Got: {result} ({status})")
    print("-" * 50)

if __name__ == "__main__":
    run_tests()