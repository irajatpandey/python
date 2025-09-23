def find_peak_element(arr: list[int]) -> int:
    # Your solution logic goes here
    pass

def run_tests_peak():
    test_cases = [
        ([1, 2, 3, 1], 2),   # Index of the peak
        ([1, 2, 1, 3, 5, 6, 4], 5), # A peak at index 5
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
    ]

    for arr, expected_index in test_cases:
        result_index = find_peak_element(arr)
        print(f"Array: {arr}")
        print(f"Expected Peak Index: {expected_index}, Got: {result_index}")
        
        # Note: A test case for peak element is usually checking if the found element is indeed a peak
        # rather than a specific index, as multiple peaks can exist.
        if arr[result_index] > arr[result_index-1] and arr[result_index] > arr[result_index+1]:
            print("✅ Test Passed!")
        else:
            print("❌ Test Failed!")
        print("-" * 20)