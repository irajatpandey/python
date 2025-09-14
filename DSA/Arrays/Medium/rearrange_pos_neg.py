from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n  # Result array with same size as nums

    pos_ptr = 0
    neg_ptr = 1

    for num in nums:
        if num > 0:
            result[pos_ptr] = num
            pos_ptr += 2
        else: # num < 0
            result[neg_ptr] = num
            neg_ptr += 2
    
    return result

# Example usage
nums1 = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums1))
# Output: [3, -2, 1, -5, 2, -4]

nums2 = [-1, 1]
print(rearrangeArray(nums2))
# Output: [1, -1]