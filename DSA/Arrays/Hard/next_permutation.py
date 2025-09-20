from typing import List

def next_permutation_brute_force(nums: List[int]) -> None:
    """
    Finds the next lexicographically greater permutation of numbers.
    This is the brute-force approach.
    It generates all permutations, sorts them, and then finds the next one.
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    all_permutation = [] # List to store all generated permutations
    
    # Recursive helper function to generate all possible permutations
    def generate_permutation(current_permutation, seen) -> None:
        # Base case: if a full-length permutation is formed
        if len(current_permutation) == n:
            all_permutation.append(list(current_permutation)) # Add a copy to the list
            return
        
        # Recursive step: iterate through all elements to build the permutation
        for i in range(n):
            # Check if the element has been used in the current permutation
            if not seen[i]:
                # Action: Choose the element
                current_permutation.append(nums[i])
                seen[i] = True
                
                # Recursive call to fill the next position
                generate_permutation(current_permutation, seen)
                
                # Backtracking: Undo the choice to explore other paths
                current_permutation.pop()
                seen[i] = False
    
    # Initial setup for recursion
    seen = [False] * n
    generate_permutation([], seen)
    
    # Sort all generated permutations lexicographically
    all_permutation.sort()
    
    # Find the index of the original 'nums' array in the sorted list of permutations
    index = None
    for i in range(len(all_permutation)):
        if all_permutation[i] == nums:
            # Handle the case of the last permutation, where we wrap around to the first
            if i + 1 != len(all_permutation):
                index = i + 1
            else:
                index = 0
            break
            
    # Modify the original 'nums' list IN-PLACE
    # This is the most crucial step as per the problem requirements
    for i in range(n):
        nums[i] = all_permutation[index][i]

## Optimized Code ##
from typing import List

def reverse_sub_array(nums: List[int], start: int, end: int) -> None:
    """Helper function to reverse a sub-array in-place."""
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def next_permutation(nums: List[int]) -> None:
    """
    Finds the next lexicographically greater permutation in-place using an optimal O(n) approach.
    """
    n = len(nums)
    
    # Step 1: Find the "pivot" point. This is the first element from the right
    # that is smaller than the element to its right.
    pivot_index = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot_index = i
            break
            
    # If no such pivot exists, the array is in descending order, so reverse it
    # to get the smallest permutation.
    if pivot_index == -1:
        reverse_sub_array(nums, 0, n - 1)
        return

    # Step 2: Find the smallest element to the right of the pivot that is
    # greater than the pivot.
    right_most_greater_index = n - 1
    while nums[right_most_greater_index] <= nums[pivot_index]:
        right_most_greater_index -= 1
        
    # Step 3: Swap the pivot and this element.
    nums[pivot_index], nums[right_most_greater_index] = nums[right_most_greater_index], nums[pivot_index]
    
    # Step 4: Reverse the sub-array to the right of the pivot.
    reverse_sub_array(nums, pivot_index + 1, n - 1)

# Driver code to test the function
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Original array: {nums}")
    # next_permutation_brute_force(nums)
    next_permutation(nums)
    print(f"Next permutation: {nums}")