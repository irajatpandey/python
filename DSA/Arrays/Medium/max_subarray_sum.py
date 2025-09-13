from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    """
    Finds the contiguous subarray with the largest sum using Kadane's Algorithm.
    """
    pass

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = max_subarray_sum(nums)
    print(f"The maximum subarray sum is: {max_sum}")
    
    nums = [5, 4, -1, 7, 8]
    max_sum = max_subarray_sum(nums)
    print(f"The maximum subarray sum is: {max_sum}")