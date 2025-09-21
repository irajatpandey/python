def largest_odd_number(num: str) -> str:
    """
    Finds the largest odd number as a substring of the given string.
    """
    n = len(num)
    for i in range(n - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return ""

if __name__ == "__main__":
    num1 = "52"
    num2 = "4206"
    print(f"Largest odd number in '{num1}': {largest_odd_number(num1)}")
    print(f"Largest odd number in '{num2}': {largest_odd_number(num2)}")