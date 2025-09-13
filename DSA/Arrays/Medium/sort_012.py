from typing import List

def sort_012(nums: List[int]) -> None:
    """
    Sorts an array containing only 0s, 1s, and 2s in-place.
    """
    pass

if __name__ == "__main__":
    nums = [0, 1, 2, 0, 1, 2, 0]
    print(f"Original array: {nums}")
    sort_012(nums)
    print(f"Sorted array: {nums}")

    nums = [2, 0, 1]
    print(f"Original array: {nums}")
    sort_012(nums)
    print(f"Sorted array: {nums}")