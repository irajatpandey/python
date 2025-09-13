def find_single_number(nums: list) -> int:
    ans = 0
    for item in nums:
        ans = ans ^ item
    return ans

if __name__ == "__main__":
    # Example data
    nums = [4, 1, 2, 1, 2]
    
    # Yahaan aapka function call hoga
    single_num = find_single_number(nums)
    print(f"The number that appears once is: {single_num}")