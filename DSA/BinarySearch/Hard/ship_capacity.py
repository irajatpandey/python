# ship_capacity.py - Capacity to ship packages within D days

from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    
    # Nested Feasibility Check Function
    def canShip(weights: List[int], days: int, capacity: int) -> bool:
        """
        Checks if all packages can be shipped within the given 'days' 
        using the specified 'capacity'.
        """
        total_weight = 0
        days_needed = 1 # Shipping always starts on Day 1
        
        for weight in weights:
            if total_weight + weight > capacity:
                # Capacity exceeded: Must start a new day
                days_needed += 1
                total_weight = weight # New day starts with the current package
            else:
                # Capacity allows: Add package to current day's load
                total_weight += weight
                
        return days_needed <= days

    # 1. Define Search Space
    # Start: Minimum required capacity (must carry the heaviest package)
    start = max(weights)
    # End: Maximum required capacity (ship all in one day)
    end = sum(weights)
    
    # 'ans' stores the smallest sufficient capacity found so far.
    ans = end 
    
    while start <= end:
        mid = start + (end - start) // 2   
        
        # 2. Feasibility Check
        possible = canShip(weights, days, mid)
        
        # 3. Adjust Pointers
        if possible:
            # Capacity 'mid' works. Store it as the best answer.
            ans = mid
            # Try for an even smaller capacity (search left).
            end = mid - 1
        else:
            # Capacity 'mid' is too small (days needed > days). Increase capacity (search right).
            start = mid + 1
            
    # 4. Return the smallest sufficient capacity found.
    return ans

if __name__ == "__main__":
    # Test execution for standalone script
    
    # Note: Removed 'self' from the function definition for this to work outside a class.
    
    test_cases = [
        # Weights, Days (D), Expected Capacity
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
        ([3, 2, 2, 4, 1, 4], 3, 6),
        ([1, 2, 3, 1, 1], 4, 3)
    ]
    
    for weights, d, expected in test_cases:
        # Calling the function without self
        result = shipWithinDays(weights, d)
        print(f"Weights: {weights}, D={d}: Expected={expected}, Got={result}")