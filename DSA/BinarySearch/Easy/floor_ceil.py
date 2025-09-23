# floor_ceil.py
def floor_in_sorted(arr, x):
    """Index of floor (greatest <= x), or -1 if none."""
    raise NotImplementedError

def ceil_in_sorted(arr, x):
    """Index of ceil (smallest >= x), or len(arr) if none."""
    raise NotImplementedError

def main():
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    _f = floor_in_sorted(arr, x)
    _c = ceil_in_sorted(arr, x)

if __name__ == "__main__":
    def test():
        cases = [
            ([1, 2, 8, 10, 10, 12, 19], 5, None, None),  # TODO
            ([2, 4, 6], 1, None, None),                  # TODO: floor -1, ceil 0
            ([2, 4, 6], 7, None, None),                  # TODO: floor last idx, ceil len(arr)
        ]
        for arr, x, ef, ec in cases:
            assert floor_in_sorted(arr, x) == ef
            assert ceil_in_sorted(arr, x) == ec
    test()
    # main()
