def lower_bound(arr: list[int], target: int):
    n = len(arr)
    start = 0
    end = n - 1
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            ans = mid
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans

def upper_bound(arr: list[int], target: int):
    n = len(arr)
    start = 0
    end = n - 1
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            ans = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans

def count_occurrences(arr: list[int], target: int) -> int:
    # Your solution logic goes here

     upperBound =  upper_bound(arr, target) 
     lowerBound =  lower_bound(arr, target) 

     if lowerBound == -1:
         return 0
     return upperBound - lowerBound + 1
   

def run_tests_count():
    test_cases = [
        ([2, 4, 10, 10, 10, 18, 20], 10, 3),
        ([5, 7, 7, 8, 8, 10], 8, 2),
        ([1, 1, 1, 1, 1, 1], 1, 6),
        ([2, 3, 4, 5], 6, 0),
        ([1, 2, 3, 4, 5], 2, 1),
    ]

    for arr, target, expected in test_cases:
        result = count_occurrences(arr, target)
        print(f"Array: {arr}, Target: {target}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)


run_tests_count()