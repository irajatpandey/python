from typing import List

def count_subarrays_with_xor_k(nums: List[int], k: int) -> int:
    """
    Counts the number of subarrays whose XOR sum is equal to K.
    """
    pass

if __name__ == "__main__":
    nums = [4, 2, 2, 6, 4]
    k = 6
    result = count_subarrays_with_xor_k(nums, k)
    print(f"Number of subarrays with XOR sum {k}: {result}")