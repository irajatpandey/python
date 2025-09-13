from typing import List

def generate_pascal_triangle(num_rows: int) -> List[List[int]]:
    """
    Generates the first num_rows of Pascal's triangle.
    """
    pass

if __name__ == "__main__":
    num_rows = 5
    triangle = generate_pascal_triangle(num_rows)
    print(f"Pascal's Triangle with {num_rows} rows:")
    for row in triangle:
        print(row)