def remove_duplicates(nums: list) -> int:
    if not nums:
        return 0

    # 'i' unique elements ka pointer hai, jo hamesha unique element ki position par rahega
    i = 0

    # 'j' list ke saare elements par iterate karega
    for j in range(1, len(nums)):
        # Agar current element (nums[j]) pichle unique element (nums[i]) se alag hai,
        # toh iska matlab yeh ek naya unique element hai.
        if nums[j] != nums[i]:
            # 'i' ko aage badha kar naye unique element ke liye jagah banayein
            i += 1
            # Naye unique element ko uss jagah par rakhein
            nums[i] = nums[j]
    
    # Unique elements ki count i + 1 hogi (kyunki i 0 se start hota hai)
    return i + 1

if __name__ == "__main__":
    # Example data
    nums = [1, 1, 2, 2, 3, 4]
    
    # Yahaan aapka function call hoga
    k = remove_duplicates(nums)
    print(f"The number of unique elements is: {k}")
    print(f"The array after removing duplicates: {nums[:k]}")