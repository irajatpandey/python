def find_missing_number(nums: list) -> int:
    
    sum = 0
    for item in nums:
        sum += item
        
    n = len(nums)
    total = (n * (n + 1)) // 2
    return total - sum

if __name__ == "__main__":
    # Example data
    nums = [3, 0, 1]
    
    # Yahaan aapka function call hoga
    missing_num = find_missing_number(nums)
    print(f"The missing number is: {missing_num}")