# search_insert.py
def search_insert(arr, x):
    """If x in arr, return index; else return insertion position."""
    raise NotImplementedError

def main():
    arr = [1, 3, 5, 6]
    x = 5
    _ = search_insert(arr, x)

if __name__ == "__main__":
    def test():
        cases = [
            ([1, 3, 5, 6], 5, None),  # TODO: found index
            ([1, 3, 5, 6], 2, None),  # TODO: insertion position
            ([], 4, None),            # TODO: 0
        ]
        for arr, x, expected in cases:
            assert search_insert(arr, x) == expected
    test()
    # main()
