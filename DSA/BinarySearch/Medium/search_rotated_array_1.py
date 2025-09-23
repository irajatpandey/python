def search_rotated(arr: list[int], target: int) -> int:
    # Your solution logic goes here
    pass

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