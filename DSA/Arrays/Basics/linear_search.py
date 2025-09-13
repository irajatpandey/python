def linear_search(li: list, target: int) -> int:
    for i in range(len(li)):
        if li[i] == target:
            return i
    return -1

if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25]
    target1 = 15
    target2 = 30

    print(f"Index of {target1} is: {linear_search(numbers, target1)}")
    print(f"Index of {target2} is: {linear_search(numbers, target2)}")