# search_insert.py
def search_insert(arr, x):
    """If x in arr, return index; else return insertion position."""
    index = len(arr)
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= x:
            index = mid
            end = mid - 1
        else:
            # covers arr[mid] < x; also advances when not >= x
            start = mid + 1
    return index


def main():
    print("Demo runs:")
    for arr, x in (
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([], 4),
    ):
        print(f"arr={arr}, x={x} -> idx={search_insert(arr, x)}")


def _self_test():
    # Minimal self-checks that won't raise without pytest
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([], 4, 0),
        ([1, 2, 4, 4, 5], 4, 2),  # first valid position for 4
    ]
    for arr, x, expected in cases:
        got = search_insert(arr, x)
        print("TEST", arr, x, "=>", got, "(expect", expected, ")")
        assert got == expected, (arr, x, got, expected)

if __name__ == "__main__":
    _self_test()
    main()
