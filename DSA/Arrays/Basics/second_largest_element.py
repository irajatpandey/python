def second_largest_element(li: list) -> int:
    if len(li) <= 1:
        return li[0]
    
    largest = float('-inf')
    second_largest = float('-inf')

    for item in li:
        if largest < item:
            second_largest = largest
            largest = item
        if largest != item and second_largest < item:
            second_largest = item
    return second_largest

if __name__ == "__main__":
    numbers = [10, 5, 20, 15, 25]
    second_largest = second_largest_element(numbers)
    print(f"The second largest element is: {second_largest}")