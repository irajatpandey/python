def search_rotated_duplicates(nums: list[int], target: int) -> bool:
    start = 0
    end = len(nums) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        # 1. Target Found
        if nums[mid] == target:
            return True
        
        # 2. Handle Duplicates (Ambiguity)
        # Jab nums[start], nums[mid], aur nums[end] same ho, toh sorted half pata nahi chalta.
        # Safety ke liye start aur end ko move kar dete hain.
        if nums[start] == nums[mid] and nums[mid] == nums[end]:
            start += 1
            end -= 1
            continue # Agli iteration par jaao
        
        # 3. Identify Sorted Half (Standard Logic)
        
        # Left Half Sorted hai: nums[start] <= nums[mid]
        if nums[start] <= nums[mid]:
            # Target Left Half mein hai: nums[start] <= target < nums[mid]
            if nums[start] <= target and target < nums[mid]:
                end = mid - 1
            else:
                # Target Right Half mein ho sakta hai
                start = mid + 1
        
        # Right Half Sorted hai: nums[mid] <= nums[end]
        else:
            # Target Right Half mein hai: nums[mid] < target <= nums[end]
            if nums[mid] < target and target <= nums[end]:
                start = mid + 1
            else:
                # Target Left Half mein ho sakta hai
                end = mid - 1
        
    return False

def run_tests_search_2():
    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0, True),
        ([2, 5, 6, 0, 0, 1, 2], 3, False),
        ([1, 0, 1, 1, 1], 0, True),
        ([1, 1, 1, 1, 1], 0, False),
        ([1, 1, 3, 1], 3, True),
    ]

    for arr, target, expected in test_cases:
        result = search_rotated_duplicates(arr, target)
        print(f"Array: {arr}, Target: {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)

run_tests_search_2()