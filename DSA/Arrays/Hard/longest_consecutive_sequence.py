from typing import List

from typing import List

def longest_consecutive_brute_force(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence using a brute force approach.
    """
    if not nums:
        return 0

    longest_streak = 0
    
    # Iterate through each number in the list
    for num in nums:
        current_num = num
        current_streak = 1
        
        # Check for consecutive numbers starting from the current number
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1
        
        # Update the longest streak found so far
        longest_streak = max(longest_streak, current_streak)
        
    return longest_streak

def longest_consecutive(nums: List[int]) -> int:
    """
    Finds the length of the longest consecutive elements sequence.
    """
    cache = {}
    for item in nums:
        cache[item] = True

    for key in cache.keys():
        if key - 1 in cache:
            cache[key] = False
    
    ans = 0

    for key in cache.keys():
        if cache[key] == True:
            count = 0
            while key in cache:
                count += 1
                ans = max(ans, count)
                key += 1
    return ans

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive(nums)
    print(f"Longest consecutive sequence length: {result}")