# aggressive_cows.py - Aggressive cows

def max_min_distance(stalls: list[int], k: int) -> int:
    # 1. Essential Step: The greedy check requires the stalls to be sorted.
    stalls.sort()
    
    def check(stalls: list[int], k: int, d: int) -> bool:
        """Checks if K cows can be placed with a minimum distance of d (mid)."""
        cows_placed = 1
        lastCowPosition = stalls[0]
        
        for i in range(1, len(stalls)):
            # If current stall is far enough from the last placed cow
            if stalls[i] - lastCowPosition >= d:
                cows_placed += 1
                lastCowPosition = stalls[i]
            
            # Optimization: If K cows are placed, we succeed early
            if cows_placed == k:
                return True
        return False
        
    # 2. Define Search Space (Based on distance)
    # Start: Minimum possible distance is 1.
    start = 1
    # End: Maximum possible distance is the distance between the first and last stall.
    end = stalls[-1] - stalls[0]
    
    ans = -1
    
    # 3. Binary Search for Maximum Minimum Distance
    while start <= end:
        mid = start + (end - start) // 2
        
        possible = check(stalls, k, mid)
        
        if possible:
            # 'mid' distance works! Store it and try for a larger distance (Maximize minimum).
            ans = mid
            start = mid + 1
        else:
            # 'mid' distance is too large. Try a smaller distance.
            end = mid - 1
            
    return ans


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4, 8, 9], 3, 3),
        ([0, 3, 4, 7, 10, 9], 4, 3),
        ([1, 2, 3, 4, 5], 2, 4)
]
    
    for stalls, k, expected in test_cases:
        result = max_min_distance(stalls, k)
        print(f"Stalls: {stalls}, K={k}: Expected={expected}, Got={result}")