from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges nums2 into nums1 without using extra space.
    Do not return anything, modify nums1 in-place instead.
    """
    pass

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"Original nums1: {nums1}")
    print(f"Original nums2: {nums2}")
    merge(nums1, m, nums2, n)
    print(f"Merged nums1: {nums1}")