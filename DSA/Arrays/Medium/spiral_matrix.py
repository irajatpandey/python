from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    
    if not matrix or not matrix[0]:
        return result
    
    rows, cols = len(matrix), len(matrix[0])
    
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while left <= right and top <= bottom:
        # 1. Left to Right (top row)
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # 2. Top to Bottom (right column)
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Check for remaining rows and columns
        if top <= bottom:
            # 3. Right to Left (bottom row)
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
        if left <= right:
            # 4. Bottom to Top (left column)
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix1)) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix2)) # Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]