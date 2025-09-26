def find_single_element(nums: list[int]) -> int:
    n = len(nums)
    if n == 1: return nums[0]
    if nums[0] != nums[1]: return nums[0]
    if nums[n - 1] != nums[n - 2]: return nums[n - 1]

    start = 1
    end = n - 2
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        
        if (mid % 2 != 0 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            start = mid + 1
        else:
            end = mid - 1
    return -1

def run_tests_single():
    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1, 1, 2], 2),
        ([2, 2, 3], 3),
        ([1, 2, 2], 1),
    ]

    for arr, expected in test_cases:
        result = find_single_element(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)

run_tests_single()