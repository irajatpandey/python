from typing import List

def sort_012(nums: List[int]) -> None:
    """
    Sorts an array containing only 0s, 1s, and 2s in-place
    using the Dutch National Flag Algorithm.
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage
nums = [0, 1, 2, 0, 1, 2]
sort_012(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

nums2 = [2, 0, 1]
sort_012(nums2)
print(nums2) # Output: [0, 1, 2]