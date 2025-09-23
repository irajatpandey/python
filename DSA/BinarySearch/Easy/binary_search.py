# binary_search.py
def search_x(arr, x):
    """Return index of x in sorted arr, or -1 if not found."""
    raise NotImplementedError

def main():
    # Driver: change inputs as needed
    arr = [1, 3, 5, 7, 9]
    x = 7
    _ = search_x(arr, x)  # TODO: print or assert

if __name__ == "__main__":
    # Minimal tests (replace expected with actual values after implementing)
    def test():
        cases = [
            ([1, 3, 5, 7, 9], 7, None),   # TODO: expected index
            ([1, 3, 5, 7, 9], 2, None),   # TODO: -1
            ([], 1, None),                # TODO
        ]
        for arr, x, expected in cases:
            assert search_x(arr, x) == expected
    test()
    # main()
