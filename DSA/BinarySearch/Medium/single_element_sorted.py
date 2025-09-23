def find_single_element(arr: list[int]) -> int:
    # Your solution logic goes here
    pass

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