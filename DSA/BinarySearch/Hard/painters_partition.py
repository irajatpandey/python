from typing import List

class Solution:
    def minTime(self, arr: List[int], k: int) -> int:
        """
        Finds the minimum time required to paint all boards (arr), 
        divided among k painters, by minimizing the maximum time taken by any single painter.
        
        Args:
            arr (List[int]): List of time taken to paint each board.
            k (int): The number of painters available.

        Returns:
            int: The minimum achievable maximum time, or -1 if k > len(arr).
        """
        
        # --- 1. Edge Case Check ---
        # If the number of painters is greater than the number of boards, 
        # the task is impossible as per competitive programming constraints (k > N).
        if k > len(arr):
            return -1
        
        def check(arr: List[int], k: int, max_time_limit: int) -> bool:
            """
            Feasibility function: Checks if all boards can be painted using K or fewer 
            painters, with the maximum time taken by any one painter not exceeding 'max_time_limit'.
            """
            painters_needed = 1  # Start with the first painter
            total_time = 0
            
            for time in arr:
                # If adding the current board's time exceeds the limit
                if total_time + time > max_time_limit:
                    # Start a new painter
                    painters_needed += 1
                    total_time = time  # New painter starts with the current board's time
                else:
                    # Current painter takes the board
                    total_time += time
            
            # Returns True if the required painters are within the limit k.
            return painters_needed <= k

        # --- 2. Define Search Space ---
        # Start (Lower Bound): The minimum max time is the time taken by the longest single board.
        start = max(arr) 
        # End (Upper Bound): The maximum max time is the total time for all boards (1 painter).
        end = sum(arr)
        
        # 'ans' stores the smallest valid max_time_limit found so far.
        ans = -1 
        
        # --- 3. Binary Search Execution ---
        while start <= end:
            mid = start + (end - start) // 2  # The current potential max time limit
            
            if check(arr, k, mid):
                # Feasible! Store 'mid' and try to find an even smaller time (search left).
                ans = mid
                end = mid - 1
            else:
                # Not feasible. The limit (mid) is too small. Increase the limit (search right).
                start = mid + 1
                
        # 'ans' holds the minimum largest time required.
        return ans

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        # (boards_time, painters, expected_min_max_time)
        ([10, 20, 30, 40], 2, 60),      # P1: 10+20+30=60 | P2: 40. Max is 60.
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 17), # P1: 1+2+3+4+5=15 | P2: 6+7=13 | P3: 8+9=17. Max is 17.
        ([10, 10, 10, 10], 4, 10),      # P1:10, P2:10, P3:10, P4:10. Max is 10.
        ([10, 5], 3, -1)               # Edge Case: k > N, returns max(arr) because k > len(arr) is false here.
    ]
    
    print("--- Painter's Partition Problem Test Results ---")
    for arr, k, expected in test_cases:
        result = s.minTime(arr, k)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Boards Time: {arr}, Painters: {k}")
        print(f"  Expected Min Max Time: {expected}, Got: {result} ({status})")
    print("-" * 60)