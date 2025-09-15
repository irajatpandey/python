from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    """
    Sets entire row and column to 0 if a cell is 0.
    Do not return anything, modify matrix in-place instead.
    """
    pass

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Original matrix:")
    for row in matrix:
        print(row)
    set_zeroes(matrix)
    print("\nMatrix after setting zeros:")
    for row in matrix:
        print(row)