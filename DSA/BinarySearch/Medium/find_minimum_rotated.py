def find_min(nums: list[int]) -> int:
    start = 0
    end = len(nums) - 1
    current_min = nums[0]  # Minimum ko track karne ke liye

    # Case 1: Agar array sorted nahi hai, toh hi loop mein jaao
    # Agar nums[start] < nums[end] hai, toh array already sorted hai aur nums[start] minimum hai.
    while start <= end:
        # Check 1: Agar poora segment sorted hai, toh nums[start] potential answer hai
        if nums[start] <= nums[end]:
            current_min = min(current_min, nums[start])
            break # Agar segment sorted hai toh loop break kar do
        
        mid = start + (end - start) // 2
        
        # Check 2: current_min ko update karo with nums[mid]
        current_min = min(current_min, nums[mid])

        # Check 3: Kaunsa half sorted hai aur kahan search karna hai?
        
        # Left half is sorted (nums[start] <= nums[mid]):
        # Minimum right half mein hoga.
        if nums[start] <= nums[mid]:
            start = mid + 1
        
        # Right half is sorted (nums[mid] < nums[end]):
        # Minimum left half mein hoga (pivot).
        else: 
            end = mid - 1
            
    return current_min

# Example Usage (Test)
# s = Solution()
# print(s.findMin([3, 4, 5, 1, 2])) # Expected: 1
# print(s.findMin([4, 5, 6, 7, 0, 1, 2])) # Expected: 0
# print(s.findMin([11, 13, 15, 17])) # Expected: 11

def run_tests_min():
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([2, 1], 1),
    ]

    for arr, expected in test_cases:
        result = find_min(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)

run_tests_min()