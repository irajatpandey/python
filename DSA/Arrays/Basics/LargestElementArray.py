
def largestElement(li: list) -> int:
    ans = float('-inf')

    for item in li:
        if item > ans:
            ans = item
    return ans


if __name__ == "__main__":
    numbers = [10, -5, 20, 8, -15]
    output = largestElement(numbers)
    print(output)