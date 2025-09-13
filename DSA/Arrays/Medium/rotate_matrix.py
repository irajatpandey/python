from typing import List

def rotate_matrix(matrix: List[List[int]]) -> None:
    """
    Rotates a square matrix by 90 degrees in a clockwise direction in-place.
    """
    pass

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