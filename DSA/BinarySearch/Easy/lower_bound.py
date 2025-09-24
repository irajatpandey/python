# lower_bound.py
def lower_bound(arr, x):
    """First index i where arr[i] >= x; return len(arr) if none."""
    
    index = None
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] >= x:
            index = mid
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
    return index


    
def main():
    arr = [1, 2, 4, 4, 5]
    x = 4
    try:
        ans = lower_bound(arr, x)
        print("lower_bound:", ans)
    except NotImplementedError:
        print("lower_bound: NOT IMPLEMENTED (OK for template)")

if __name__ == "__main__":
    main()
