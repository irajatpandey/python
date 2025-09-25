def search_rotated(nums: list[int], target: int) -> int:

    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[start] <= nums[mid]:
            if nums[start] <= target and target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] <= target and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        
    return -1

def run_tests_search_1():
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 1, 0),
        ([1, 3], 3, 1),
        ([3, 1], 1, 1),
    ]

    for arr, target, expected in test_cases:
        result = search_rotated(arr, target)
        print(f"Array: {arr}, Target: {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)


run_tests_search_1()