from typing import List


def find_duplicate_sum(nums: List[int]) -> int:
    """
    Finds the duplicate number using the sum of numbers approach.
    Time: O(N), Space: O(1).
    """
    n = len(nums) - 1 # N is the size of the set of numbers (1 to N)
    
    # Expected sum using the arithmetic progression formula: n*(n+1)/2
    expected_sum = n * (n + 1) // 2

    # Actual sum of the numbers in the list
    actual_sum = sum(nums)

    # The difference is the duplicate number
    return actual_sum - expected_sum

def find_duplicate(nums: List[int]) -> int:
    """
    Finds the duplicate number in an array of N+1 integers.
    The array contains numbers from 1 to N.
    """

    cache = {}
    for item in nums:
        if item in cache:
            cache[item] += 1
        else:
            cache[item] = 1
    
    for item in nums:
        if cache[item] > 1:
            return item

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    duplicate = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate}")

    nums = [3, 1, 3, 4, 2]
    duplicate = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate}")

    nums = [1, 3, 4, 2, 2]
    duplicate = find_duplicate_sum(nums)
    print(f"The duplicate number (sum approach) is: {duplicate}")