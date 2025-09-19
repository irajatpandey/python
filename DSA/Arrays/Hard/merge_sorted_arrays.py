from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merges nums2 into nums1 without using extra space.
    Do not return anything, modify nums1 in-place instead.
    """

    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1

    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1

    

    

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(f"Original nums1: {nums1}")
    print(f"Original nums2: {nums2}")
    merge(nums1, m, nums2, n)
    print(f"Merged nums1: {nums1}")