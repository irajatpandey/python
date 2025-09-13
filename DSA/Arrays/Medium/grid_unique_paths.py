def unique_paths(m: int, n: int) -> int:
    """
    Calculates the number of unique paths from the top-left corner to the 
    bottom-right corner of an m x n grid. You can only move down or right.
    """
    pass

if __name__ == "__main__":
    m, n = 3, 7
    paths = unique_paths(m, n)
    print(f"Number of unique paths for a {m}x{n} grid: {paths}")

    m, n = 3, 2
    paths = unique_paths(m, n)
    print(f"Number of unique paths for a {m}x{n} grid: {paths}")