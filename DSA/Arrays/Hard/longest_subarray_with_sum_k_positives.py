from typing import List

def longest_subarray_with_sum_k_positives(nums: List[int], k: int) -> int:
    """
    Finds the length of the longest subarray with a given sum K.
    (Assumes all numbers are positive)
    """
    pass

if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1, 1, 1, 3]
    k = 3
    result = longest_subarray_with_sum_k_positives(nums, k)
    print(f"Longest subarray with sum {k}: {result}")