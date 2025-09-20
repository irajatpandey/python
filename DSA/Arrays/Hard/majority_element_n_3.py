from typing import List

def majorityElementII(nums: List[int]) -> List[int]:
    """
    Return all elements appearing strictly more than floor(n/3) times.
    Uses extended Boyer–Moore with two candidates + validation.
    """
    candidate1 = None
    candidate2 = None
    count1 = 0
    count2 = 0

    for ele in nums:
        if ele == candidate1:
            count1 += 1
        elif ele == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = ele
            count1 = 1
        elif count2 == 0:
            candidate2 = ele
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
        
    res = []
    cnt1 = sum(1 for x in nums if x == candidate1) if candidate1 is not None else 0
    cnt2 = sum(1 for x in nums if x == candidate2) if candidate2 is not None else 0
    n = len(nums)
    if cnt1 > n // 3:
        res.append(candidate1)
        
    if candidate2 is not None and candidate1 != candidate2 and cnt2 > n // 3:
        res.append(candidate2)
    return res

def run_tests():
    # Each: (input, expected). Expected sorted.
    tests = [
        ([3, 2, 3], [3]),                                   # Example [web:17]
        ([1, 1, 1, 3, 3, 2, 2, 2], [1, 2]),                 # Example [web:17][web:8]
        ([], []),                                           # Empty [web:24]
        ([1], [1]),                                         # Single [web:24]
        ([1, 2], [1, 2]),                                       # No element > n/3 [web:24]
        ([1, 2, 3], []),                                    # All distinct [web:24]
        ([2, 2, 2, 2], [2]),                                # One element dominates [web:24]
        ([1, 2, 2, 3, 2, 1, 1, 3], [1, 2]),                 # Two valid answers [web:24][web:64]
        ([1, 1, 2, 2, 3, 3], []),                           # None > n/3 [web:24]
        ([0, 0, 0, 1, 2, 3], [0]),                          # Zero cases [web:24]
        ([4, 4, 4, 4, 5, 5, 5], [4, 5]),                       # Only one > n/3 [web:24]
        ([2, 2, 1, 3], [2]),                                # 2 appears 2 > 4/3 (=1) [web:24]
        ([1, 2, 2, 2, 3, 3, 3], [3, 2]),                    # Both cross threshold [web:24][web:64]
        ([1, 1, 1, 1, 2, 3, 4, 5], [1]),                    # One strong majority [web:24]
        ([1, 2, 2, 3, 3, 3, 4, 4, 4], []),              # Two near-equal majorities [web:24]
    ]

    passed = 0
    for i, (arr, expected) in enumerate(tests, 1):
        got = majorityElementII(arr)
        status = "OK" if got == expected else "FAIL"
        print(f"Test {i}: {status} | input={arr} expected={expected} got={got}")
        passed += (got == expected)
    print(f"Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    run_tests()
