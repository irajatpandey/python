def find_min(arr: list[int]) -> int:
    # Your solution logic goes here
    pass

def run_tests_min():
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([2, 1], 1),
    ]

    for arr, expected in test_cases:
        result = find_min(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)