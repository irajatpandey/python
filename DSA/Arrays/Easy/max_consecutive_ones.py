def max_consecutive_ones(nums: list) -> int:
    max_ones = 0 
    count = 0

    for item in nums:
        if item == 1:
            count += 1
        else:
            count = 0
        max_ones = max(max_ones, count)
    return max_ones

if __name__ == "__main__":
    # Example data
    nums = [1, 1, 0, 1, 1, 1]
    
    # Yahaan aapka function call hoga
    max_ones = max_consecutive_ones(nums)
    print(f"The maximum consecutive ones are: {max_ones}")