from typing import List

def find_duplicate(nums: List[int]) -> int:
    """
    Finds the duplicate number in an array of N+1 integers.
    The array contains numbers from 1 to N.
    """
    pass

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    duplicate = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate}")

    nums = [3, 1, 3, 4, 2]
    duplicate = find_duplicate(nums)
    print(f"The duplicate number is: {duplicate}")