from typing import List

def longest_subarray_with_sum_k(nums: List[int], k: int) -> int:
    maxLength = 0
    for i in range(len(nums)):
        currentSum = 0
        for j in range(i, len(nums)):
            currentSum += nums[j]
            if currentSum == k:
                maxLength = max(maxLength, j - i + 1)
    return maxLength

if __name__ == "__main__":
    nums = [10, 5, 2, 7, 1, 9]
    k = 15
    result = longest_subarray_with_sum_k(nums, k)
    print(f"Longest subarray with sum {k}: {result}")