from typing import List

def max_subarray_with_sum(nums: List[int]) -> List[int]:
    """
    Finds the contiguous subarray with the largest sum and returns that subarray.
    """
    pass

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_subarray = max_subarray_with_sum(nums)
    print(f"The subarray with the maximum sum is: {max_subarray}")
    
    nums = [5, 4, -1, 7, 8]
    max_subarray = max_subarray_with_sum(nums)
    print(f"The subarray with the maximum sum is: {max_subarray}")