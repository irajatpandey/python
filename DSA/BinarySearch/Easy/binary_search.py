# binary_search.py
def search_x(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return None

def main():
    # Driver: change inputs as needed
    arr = [1, 3, 5, 7, 9]
    x = 7
    # Corrected: Print the result to see the output
    print(f"Searching for {x} in {arr}: Found at index {search_x(arr, x)}")

if __name__ == "__main__":
    # Corrected tests with proper expected values
    def test():
        cases = [
            ([1, 3, 5, 7, 9], 7, 3),   # Expected index is 3
            ([1, 3, 5, 7, 9], 2, None), # Expected value is None (not found)
            ([], 1, None),               # Expected value is None (empty array)
        ]
        for arr, x, expected in cases:
            result = search_x(arr, x)
            print(f"Test case: arr={arr}, x={x}, Expected={expected}, Got={result}")
            assert result == expected
            print("Test passed!")
    test()
    main() # Call main after the tests