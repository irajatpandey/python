def find_occurrence(arr: list[int], target: int, find_first: bool) -> int:
    # Your solution logic goes here
    pass

def run_tests_first_last():
    test_cases = [
        ([2, 4, 10, 10, 10, 18, 20], 10, True, 2), # First occurrence
        ([2, 4, 10, 10, 10, 18, 20], 10, False, 4),# Last occurrence
        ([5, 7, 7, 8, 8, 10], 6, True, -1),      # Target not found
        ([5, 7, 7, 8, 8, 10], 8, True, 3),       # First occurrence of 8
        ([5, 7, 7, 8, 8, 10], 8, False, 4),      # Last occurrence of 8
    ]

    for arr, target, find_first, expected in test_cases:
        result = find_occurrence(arr, target, find_first)
        print(f"Array: {arr}, Target: {target}, Find First: {find_first}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)