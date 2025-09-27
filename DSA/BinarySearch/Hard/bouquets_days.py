# bouquets_days.py - Minimum days to make M bouquets

def min_days_to_make_bouquets(bloomDay: list[int], m: int, k: int) -> int:
    """
    Stub function to find the minimum number of days required to make M bouquets,
    where each bouquet needs K adjacent flowers.
    (Solution logic goes here)
    """
    # Example: bloomDay=[1,10,3,10,2], m=3, k=1. Result: 10 (day 10 makes 3 bouquets)

    # 1. Initial Feasibility Check: Not enough flowers to make M bouquets of K size.
    if m * k > len(bloomDay):
        return -1
    
    def check(bloomDay, m, k, mid): 
        """Checks if M bouquets can be made by day 'mid'."""
        total_bouquets = 0
        consecutive_bloomed = 0 # Tracks adjacent available flowers
        
        for day in bloomDay:
            if mid >= day:
                # Flower has bloomed, maintain adjacency chain
                consecutive_bloomed += 1
            else:
                # Adjacency chain broken, reset the counter
                consecutive_bloomed = 0
            
            # Check if a bouquet is complete
            if consecutive_bloomed == k:
                total_bouquets += 1
                consecutive_bloomed = 0 # Start tracking for the next bouquet
            
            if total_bouquets >= m:
                return True
        return False

        # --- Binary Search Setup (Optimized) ---
        # Start: Earliest bloom day (min possible answer)
        # End: Latest bloom day (max possible answer)
    start, end = min(bloomDay), max(bloomDay)
    ans = -1 # Use -1 instead of float('inf') for integer day index
    
    while start <= end:
        mid = start + (end - start) // 2

        possible = check(bloomDay, m, k, mid)       
        
        if possible:
            # Valid day, store it, and try for an earlier day (search left)
            ans = mid
            end = mid - 1
        else:
            # Invalid day, must wait longer (search right)
            start = mid + 1
            
    return ans

if __name__ == "__main__":
    test_cases = [
        ([1, 10, 3, 10, 2], 3, 1, 10),
        ([7, 7, 7, 7, 12, 7, 7], 2, 3, 12),
        ([1, 1, 1, 1, 1, 1, 1], 4, 2, -1) # Not possible
    ]
    
    for days, m, k, expected in test_cases:
        result = min_days_to_make_bouquets(days, m, k)
        print(f"Days: {days}, M={m}, K={k}: Expected={expected}, Got={result}")