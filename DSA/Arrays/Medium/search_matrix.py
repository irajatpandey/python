from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    Searches for a target value in an m x n integer matrix.
    The matrix has the following properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.
    """
    for ls in matrix:
        for item in ls:
            if item == target:
                return True
    return False 

if __name__ == "__main__":
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target1 = 3
    found1 = searchMatrix(matrix1, target1)
    print(f"Is {target1} in the matrix? {found1}")

    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    target2 = 13
    found2 = searchMatrix(matrix2, target2)
    print(f"Is {target2} in the matrix? {found2}")