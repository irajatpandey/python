def move_zeros_to_end(nums: list) -> None:
    i = 0
    j = 0

    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
       

if __name__ == "__main__":
    # Example data
    nums = [0, 1, 0, 3, 12]
    
    # Yahaan aapka function call hoga
    move_zeros_to_end(nums)
    print(f"The array after moving zeros is: {nums}")