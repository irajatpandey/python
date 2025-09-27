from typing import List

def find_peak_element(nums: List[int]) -> int:
    # Handle single element case separately
    if len(nums) == 1:
        return 0
        
    start = 0
    end = len(nums) - 1
    
    # Loop should continue until start and end meet
    while start < end:
        mid = start + (end - start) // 2
        
        # Climbing Upwards: Peak must be in the right half
        # mid + 1 < n check is NOT needed here because end = n-1, so mid is safe
        if nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            # Descending or Peak: Peak is at mid or in the left half
            end = mid
            
    # When loop terminates, start == end, which is the index of the peak.
    return start

def run_tests_peak():
    # Note: Expected index is just one of the possible peak indices.
    test_cases = [
        ([1, 2, 3, 1], 2),   
        ([1, 2, 1, 3, 5, 6, 4], 5), 
        ([1], 0),
        ([1, 2], 1), # Peak is 2 at index 1
        ([2, 1], 0), # Peak is 2 at index 0
    ]

    for i, (arr, expected_index) in enumerate(test_cases):
        result_index = find_peak_element(arr)
        
        # --- SAFE PEAK VALIDATION LOGIC ---
        is_peak = True
        n = len(arr)

        if n > 1:
            # Check Left Neighbor (if it exists)
            if result_index > 0 and arr[result_index] <= arr[result_index - 1]:
                is_peak = False
            
            # Check Right Neighbor (if it exists)
            if result_index < n - 1 and arr[result_index] <= arr[result_index + 1]:
                is_peak = False
        
        # --- Output ---
        print(f"--- Test Case {i+1} ---")
        print(f"Array: {arr}")
        print(f"Found Peak Index: {result_index}")
        
        # We check against a boolean because multiple peaks might exist.
        if is_peak:
            print("✅ Test Passed! (Found a valid peak)")
        else:
            print("❌ Test Failed! (Did not find a valid peak)")
        print("-" * 20)

        
run_tests_peak()