from typing import List

def generate_pascal_triangle(n : int) -> List[List[int]]:
    """
    Generates the first num_rows of Pascal's triangle.
    """
    output = [[1]]
    if n == 1:
        return [[1]]

    for i in range(1, n):
        smallOutput = [1]

        compute_list = output[-1]

        for j in range(len(compute_list) - 1):
            smallOutput.append(compute_list[j] + compute_list[j + 1])

        smallOutput.append(1)
        output.append(smallOutput)
    return output
    

if __name__ == "__main__":
    num_rows = 5
    triangle = generate_pascal_triangle(num_rows)
    print(f"Pascal's Triangle with {num_rows} rows:")
    for row in triangle:
        print(row)