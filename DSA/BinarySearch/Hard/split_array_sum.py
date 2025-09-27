# split_array_sum.py - Split array - largest sum

def split_array_largest_sum(nums: list[int], k: int) -> int:
    """
    Stub function to split the array into K non-empty contiguous subarrays
    such that the largest sum among these K subarrays is minimized.
    (Solution logic goes here)
    """
    # Example: nums=[7,2,5,10,8], k=2. Result: 18 ([7,2,5] | [10,8] -> max sum is 18)
    return 0

if __name__ == "__main__":
    test_cases = [
        ([7, 2, 5, 10, 8], 2, 18),
        ([1, 2, 3, 4, 5], 2, 9), # [1,2,3] | [4,5]
        ([10, 5, 13, 4, 7, 9, 10], 4, 19)
    ]
    
    for nums, k, expected in test_cases:
        result = split_array_largest_sum(nums, k)
        print(f"Nums: {nums}, K={k}: Expected={expected}, Got={result}")