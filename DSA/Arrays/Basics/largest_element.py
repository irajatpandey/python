def largest_element(li: list) -> int:
    ans = float('-inf')
    for item in li:
        if item > ans:
            item = ans
    return ans

if __name__ == "__main__":
    numbers = [10, -5, 20, 8, -15]
    largest_num = largest_element(numbers)
    print(f"The largest element is: {largest_num}")