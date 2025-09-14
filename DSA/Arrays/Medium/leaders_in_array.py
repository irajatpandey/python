from typing import List

def find_leaders(nums: List[int]) -> List[int]:
    """
    Finds all the leaders in an numsay. A leader is an element that is
    greater than all the elements to its right.
    """
    n = len(nums)
    if n == 0:
        return []
        
    output = []
    
    # Rightmost element is always a leader
    max_from_right = nums[n - 1]
    output.append(max_from_right)
    
    # Iterate from the second last element to the beginning
    for i in range(n - 2, -1, -1):
        if nums[i] >= max_from_right:
            max_from_right = nums[i]
            output.append(max_from_right)
            

    output.reverse()
    return output

if __name__ == "__main__":
    nums = [16, 17, 4, 3, 5, 2]
    leaders = find_leaders(nums)
    print(f"The leaders in the numsay are: {leaders}")

    nums = [10, 2, 4, 1, 3, 5]
    leaders = find_leaders(nums)
    print(f"The leaders in the numsay are: {leaders}")