from typing import List

def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a square matrix by 90 degrees in a clockwise direction in-place.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    # Swap elements across the main diagonal
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    rotate_matrix(matrix)
    print("\nRotated Matrix:")
    for row in matrix:
        print(row)