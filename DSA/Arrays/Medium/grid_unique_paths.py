def find_paths_helper(row: int, col: int, m: int, n: int) -> int:
    """
    Yeh ek helper function hai jo recursion ka use karke paths dhundhta hai.
    """
    # Base case 1: Target tak pahunch gaye.
    if row == m - 1 and col == n - 1:
        return 1
    
    # Base case 2: Grid se bahar nikal gaye.
    if row >= m or col >= n:
        return 0
        
    # Recursive calls: down aur right jaake paths count karo.
    down_paths = find_paths_helper(row + 1, col, m, n)
    right_paths = find_paths_helper(row, col + 1, m, n)
    
    return down_paths + right_paths

def unique_paths(m: int, n: int) -> int:
    """
    Main function jo unique paths ko calculate karta hai.
    """
    # Helper function ko top-left corner (0, 0) se start karte hue call karein.
    return find_paths_helper(0, 0, m, n)

if __name__ == "__main__":
    m, n = 3, 7
    paths = unique_paths(m, n)
    print(f"Number of unique paths for a {m}x{n} grid: {paths}")

    m, n = 3, 2
    paths = unique_paths(m, n)
    print(f"Number of unique paths for a {m}x{n} grid: {paths}")