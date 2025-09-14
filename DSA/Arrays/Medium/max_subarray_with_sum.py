from typing import List

def max_subarray_with_sum(nums: List[int]) -> List[int]:
    """
    Finds the contiguous subarray with the largest sum and returns that subarray.
    """
    # max_sum_so_far ko pehle element par set karein, aur current_sum ko bhi
    max_sum_so_far = nums[0]
    current_sum = nums[0]
    
    # Indices ko track karne ke liye variables
    start_index = 0
    end_index = 0
    temp_start_index = 0
    
    # Dusre element se loop shuru karein
    for i in range(1, len(nums)):
        num = nums[i]
        
        # Sahi logic: naye subarray se shuru karein ya current ko continue karein
        if num > current_sum + num:
            current_sum = num
            temp_start_index = i
        else:
            current_sum += num
        
        # Agar current_sum, max_sum se bada hai, to max_sum aur indices ko update karein
        if current_sum > max_sum_so_far:
            max_sum_so_far = current_sum
            start_index = temp_start_index
            end_index = i
            
    return nums[start_index : end_index + 1]

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_subarray = max_subarray_with_sum(nums)
    print(f"The subarray with the maximum sum is: {max_subarray}")
    
    nums = [5, 4, -1, 7, 8]
    max_subarray = max_subarray_with_sum(nums)
    print(f"The subarray with the maximum sum is: {max_subarray}")

    nums = [-2, -1, -5, -3]
    max_subarray = max_subarray_with_sum(nums)
    print(f"The subarray with the maximum sum is: {max_subarray}")