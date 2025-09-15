from typing import List

def longest_subarray_with_sum_k(nums: List[int], k: int) -> int:
    """
    Finds the length of the longest subarray with a given sum K.
    (Handles both positive and negative numbers)
    """
    pass

if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    result = longest_subarray_with_sum_k(nums, k)
    print(f"Longest subarray with sum {k}: {result}")