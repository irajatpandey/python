from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    """
    Finds the contiguous subarray with the largest sum using Kadane's Algorithm.
    """

    max_sum_so_far = float("-inf")
    current_sum = 0

    for item in nums:
        current_sum = max(current_sum + item, item)
        max_sum_so_far = max(max_sum_so_far, current_sum)

    return max_sum_so_far

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(nums)
    print(f"The maximum subarray sum is: {max_sum}")
    
    nums = [5, 4, -1, 7, 8]
    max_sum = max_subarray_sum(nums)
    print(f"The maximum subarray sum is: {max_sum}")