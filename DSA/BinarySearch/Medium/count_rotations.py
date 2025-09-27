def count_rotations(arr: list[int]) -> int:
    n = len(arr)
    
    # Handle the trivial case where the array has only one element.
    if n == 1:
        return 0
        
    # 'ans' stores the index of the minimum element found so far.
    # This index is the number of rotations (K).
    ans = 0 
    start = 0
    end = n - 1
    
    while start <= end:
        
        # --- Case 1: Array Segment is Sorted ---
        # If the segment from 'start' to 'end' is sorted (no rotation in this segment), 
        # the minimum element must be at 'arr[start]'.
        if arr[start] <= arr[end]:
            # Update 'ans' only if arr[start] is less than the current global minimum (arr[ans]).
            if arr[start] < arr[ans]:
                ans = start
            break # Since the segment is sorted, we can safely stop searching.
        
        # --- Binary Search Step ---
        mid = start + (end - start) // 2
        
        # --- Case 2: Update Minimum at Midpoint ---
        # Always check if the midpoint is the new overall minimum.
        if arr[mid] < arr[ans]:
            ans = mid
            
        # --- Case 3: Elimination (Identify Sorted Half) ---
        
        # Check if the Left half is sorted (from arr[start] to arr[mid])
        if arr[start] <= arr[mid]:
            # If the left half is sorted, the minimum must lie in the Right (unsorted) half.
            # Discard the left half.
            start = mid + 1
        
        # Else, the Right half must be sorted
        else: 
            # If the right half is sorted, the minimum must lie in the Left (unsorted) half.
            # Discard the right half.
            end = mid - 1
            
    # The index of the minimum element ('ans') is the number of rotations (K).
    return ans

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


run_tests_rotations()