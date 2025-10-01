def minMaxDist(self, stations, k):
        def check(stations, k, max_dist) -> bool:
            stations_needed = 0
            
            # Note: We must ensure max_dist (mid) is not 0 for division.
            if max_dist == 0:
                # If mid is 0, we need infinite stations unless all gaps are 0.
                return False 
                
            for i in range(len(stations) - 1):
                gap = stations[i + 1] - stations[i]
                
                # If gap exceeds the max allowed distance, calculate new stations required.
                if gap > max_dist:
                    # Required Stations = ceil(Gap / Max_Dist) - 1
                    new_stations_count = math.ceil(gap / max_dist) - 1
                    stations_needed += new_stations_count
                    
            return stations_needed <= k

            # 2. Define Search Space (Float Bounds)
            
            # Calculate max gap for the upper bound
        max_gap = 0.0
        for i in range(len(stations) - 1):
            max_gap = max(max_gap, stations[i + 1] - stations[i])
            
        start = 0.0
        end = max_gap
        
        # 3. Binary Search for Float Answer (Using Fixed Iterations for Precision)
        # We run the loop for a fixed number of times (e.g., 100) instead of start <= end 
        # to guarantee precision and avoid infinite loops with float arithmetic.
        
        for _ in range(100): 
            mid = start + (end - start) / 2.0
            
            if check(stations, k, mid):
                # Works! Store mid and try to minimize (search left).
                end = mid
            else:
                # Doesn't work. Increase the distance (search right).
                start = mid
                
        # After 100 iterations, 'end' will hold the minimum achievable maximum distance 
        # with high precision.
        return round(end, 5) # Return with reasonable precision