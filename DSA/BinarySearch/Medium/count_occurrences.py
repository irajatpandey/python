def count_occurrences(arr: list[int], target: int) -> int:
    # Your solution logic goes here
    pass

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