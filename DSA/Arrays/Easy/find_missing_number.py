def remove_duplicates(nums: list) -> int:
    pass

if __name__ == "__main__":
    # Example data
    nums = [1, 1, 2, 2, 3, 4]
    
    # Yahaan aapka function call hoga
    k = remove_duplicates(nums)
    print(f"The number of unique elements is: {k}")
    print(f"The array after removing duplicates: {nums[:k]}")