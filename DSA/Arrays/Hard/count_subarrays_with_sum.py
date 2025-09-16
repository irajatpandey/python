from typing import List

def count_subarrays_with_sum(nums: List[int], k: int) -> int:
    """
    Counts the number of subarrays with a given sum K.
    """
    mp = {0 : 1}
    count = 0
    current_sum = 0

    for val in nums:
        current_sum += val
        if current_sum - k in mp:
            count += mp[current_sum - k]

        mp[current_sum] = mp.get(current_sum, 0) + 1

    return count

if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    result = count_subarrays_with_sum(nums, k)
    print(f"Number of subarrays with sum {k}: {result}")