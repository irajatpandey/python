# koko_bananas.py - Koko Eating Bananas
import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    
    # Check for trivial case where H is insufficient for even the largest pile at speed 1
    # Though not strictly necessary, it avoids edge case complexity.
    if h < len(piles):
        # Time required even if Koko eats one banana per hour is len(piles).
        # If H is less than the number of piles, it's impossible.
        # Problem constraints usually guarantee a solution, but this check is good practice.
        pass
    
    # --- Initialization of Search Space (K) ---
    
    # 1. Start: The minimum possible eating speed is 1.
    start = 1 
    
    # 2. End: The maximum speed is the largest pile, as Koko can't eat faster than the biggest pile in one hour.
    end = max(piles) 
    
    # 'min_speed' will store the best (smallest) valid speed found.
    min_speed = end

    while start <= end:
        mid_speed = start + (end - start) // 2
        
        # --- Calculate Total Time for current 'mid_speed' (Feasibility Check) ---
        time_taken = 0
        
        for banana_count in piles:
            # Calculate time: ceil(piles[i] / K) gives the hours needed for each pile.
            # We use (banana_count + mid_speed - 1) // mid_speed as a robust integer division equivalent to math.ceil(a/b).
            time_taken += (banana_count + mid_speed - 1) // mid_speed
            
        # --- Binary Search Decision ---
        
        # Case 1: Time is acceptable (time_taken <= h)
        if time_taken <= h:
            # This mid_speed is valid. Store it as the best answer found so far.
            min_speed = mid_speed 
            # Try to find a smaller valid speed in the left half.
            end = mid_speed - 1        
        
        # Case 2: Time is too long (time_taken > h)
        else:
            # Speed is too slow, must increase speed.
            start = mid_speed + 1
            
    return min_speed
    
if __name__ == "__main__":
    # Remove 'self' from the function definition for this standalone script to work.
    
    # Note on math.ceil: I replaced math.ceil with integer arithmetic: (a + b - 1) // b
    # This keeps the code robust and avoids the float operation overhead.
    
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
        ([3, 6, 7, 11], 6, 6), # Additional check
    ]
    
    for piles, h, expected in test_cases:
        # Calling the function without 'self'
        result = minEatingSpeed(piles, h)
        print(f"Piles: {piles}, H={h}: Expected={expected}, Got={result}")