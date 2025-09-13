from typing import List

def find_leaders(nums: List[int]) -> List[int]:
    """
    Finds all the leaders in an array. A leader is an element that is
    greater than all the elements to its right.
    """
    pass

if __name__ == "__main__":
    nums = [16, 17, 4, 3, 5, 2]
    leaders = find_leaders(nums)
    print(f"The leaders in the array are: {leaders}")

    nums = [10, 2, 4, 1, 3, 5]
    leaders = find_leaders(nums)
    print(f"The leaders in the array are: {leaders}")