# upper_bound.py
def upper_bound(arr, x):
    """First index i where arr[i] > x; return len(arr) if none."""
    raise NotImplementedError

def main():
    arr = [1, 2, 4, 4, 5]
    x = 4
    _ = upper_bound(arr, x)

if __name__ == "__main__":
    def test():
        cases = [
            ([1, 2, 4, 4, 5], 4, None),  # TODO: first index > 4
            ([1, 2, 3], 3, None),        # TODO: len(arr)
            ([1, 1, 1], 1, None),        # TODO
        ]
        for arr, x, expected in cases:
            assert upper_bound(arr, x) == expected
    test()
    # main()
