# Majority Element (> n/2) - Driver with Embedded Tests Only (no stdin)

from typing import List

def majorityElement(nums: List[int]) -> int:
    """
    TODO: Implement and return the element that appears more than n//2 times.
    If no such element exists, return -1 (general version).
    """
    # Write your solution here
    candidate = 0
    count = 0

    for ele in nums:
        if count == 0:
            candidate = ele
            count = 1
        elif candidate == ele:
            count += 1
        else:
            count -= 1
    # Step 2: Validate the candidate
    # The first loop only finds a potential candidate. 
    # This step checks if it is truly the majority element.
    final_count = 0
    for num in nums:
        if num == candidate:
            final_count += 1
    
    if final_count > len(nums) // 2:
        return candidate
    else:
        return -1
    #raise NotImplementedError("Implement majorityElement")

def run_tests():
    tests = [
        # (input, expected)
        ([3, 2, 3], 3),                          # LeetCode example [web:9]
        ([2, 2, 1, 1, 1, 2, 2], 2),              # LeetCode example [web:9]
        ([1, 1, 1, 2, 3], 1),                    # Majority exists [web:18]
        ([10], 10),                              # Single element [web:9]
        ([5, 5], 5),                             # Pair same [web:9]
        ([5, 6], -1),                            # No majority (general case) [web:18]
        ([4, 4, 4, 2, 4, 3], 4),                 # Even length with majority [web:18]
        ([9, 9, 9, 1, 2, 9, 3, 9], 9),           # Clustered majority [web:18]
        ([2, 2, 2, 2, 1, 1, 3, 4, 5], -1),        # Odd length majority [web:18]
        ([1, 2, 3, 4, 5], -1),                   # No majority [web:18]
        ([1, 2, 2, 3, 3, 1], -1),                # Balanced, no majority [web:18]
        ([6, 6, 6, 6, 6, 1, 2, 3, 6, 5], 6),     # Heavy majority [web:18]
        ([0, 0, 1, 0, 2, 0, 3, 0, 4, 0, 0], 0),  # 0 as majority [web:18],
    ]

    passed = 0
    for i, (arr, expected) in enumerate(tests, 1):
        try:
            got = majorityElement(arr)
        except NotImplementedError as e:
            print(f"Test {i}: SKIPPED -> {e}")  # Keeps driver runnable pre-solution [web:33]
            continue
        status = "OK" if got == expected else "FAIL"
        print(f"Test {i}: {status} | input={arr} expected={expected} got={got}")
        passed += (got == expected)
    total = len(tests)
    print(f"Passed {passed}/{total} tests")

if __name__ == "__main__":
    # Always run embedded tests; no user input is read
    run_tests()
