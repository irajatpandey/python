#Time Complexity: O(n)
#Space Complexity: O(n)
def two_sum(nums: list, target: int) -> list:
    lookup = {}
    output = []
    for i in range(len(nums)):
        if target - nums[i] in lookup:
            output.append(lookup[target - nums[i]])
            output.append(i)
            return output
        else:
            lookup[nums[i]] = i
    return output 

if __name__ == "__main__":
    # Example data
    nums = [2, 7, 11, 15]
    target = 9
    
    indices = two_sum(nums, target)
    print(f"The indices of the two numbers are: {indices}")