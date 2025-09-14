from typing import List

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

   