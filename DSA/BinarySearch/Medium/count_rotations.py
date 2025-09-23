def count_rotations(arr: list[int]) -> int:
    # Your solution logic goes here
    pass

def run_tests_rotations():
    test_cases = [
        ([15, 18, 2, 3, 6, 12], 2),
        ([7, 9, 11, 12, 5], 4),
        ([1, 2, 3, 4, 5], 0),
        ([5, 1, 2, 3, 4], 1),
        ([2, 3, 4, 5, 1], 4),
    ]

    for arr, expected in test_cases:
        result = count_rotations(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 20)