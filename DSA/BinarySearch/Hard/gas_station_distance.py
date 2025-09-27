# gas_station_distance.py - Minimize max distance to gas station

def min_max_gas_distance(stations: list[int], k: int) -> float:
    """
    Stub function to minimize the maximum distance between adjacent gas stations 
    after adding K new gas stations.
    (Solution logic goes here)
    """
    # Example: stations=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=9. Result: 0.5
    return 0.0

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 0.5),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 9, 5.0),
        ([1, 2, 4, 8, 10], 1, 3.0) # Add a station between 4 and 8. Max dist becomes 3.
    ]
    
    for stations, k, expected_approx in test_cases:
        result = min_max_gas_distance(stations, k)
        print(f"Stations: {stations}, K={k}: Expected Approx={expected_approx}, Got={result}")