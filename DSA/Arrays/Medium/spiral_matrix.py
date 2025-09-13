from typing import List

def spiral_print(matrix: List[List[int]]) -> List[int]:
    """
    Prints the elements of a matrix in a spiral order.
    """
    pass

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    spiral_list = spiral_print(matrix)
    print(f"The spiral order of the matrix is: {spiral_list}")