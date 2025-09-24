# floor_ceil.py
def floor_in_sorted(arr, x):
    """Index of floor (greatest <= x), or -1 if none."""

    n = len(arr)
    start = 0
    end = n - 1
    output = None

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] <= x:
            output = arr[mid]
            start = mid + 1

        elif arr[mid] > x:
            end = mid - 1
    
    return output

def ceil_in_sorted(arr, x):
    """Index of ceil (smallest >= x), or len(arr) if none."""
    n = len(arr)
    start = 0
    end = n - 1
    output = None

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= x:
            output = arr[mid]
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
    return output    


def main():
    arr = [3, 4, 4, 7, 8, 10]
    x = 8
    try:
        f = floor_in_sorted(arr, x)
        c = ceil_in_sorted(arr, x)
        
        print("floor:", f, "ceil:", c)
    except NotImplementedError:
        print("floor/ceil: NOT IMPLEMENTED (OK for template)")

if __name__ == "__main__":
    main()



