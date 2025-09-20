from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    """
    Sets entire row and column to 0 if a cell is 0.
    Do not return anything, modify matrix in-place instead.
    """
    rows_to_zero = set()
    cols_to_zero = set()

    # Pehla Pass: Zeros ki locations dhoondo
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows_to_zero.add(r)
                cols_to_zero.add(c)
    
    # Doosra Pass: Matrix ko update karo based on locations
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows_to_zero or c in cols_to_zero:
                matrix[r][c] = 0

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    set_zeroes(matrix)
    print("\nMatrix after setting zeros:")
    for row in matrix:
        print(row)