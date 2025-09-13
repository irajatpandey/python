def left_rotate_array(li: list) -> list:
    """
    Rotates an array to the left by one position.
    """

    first_element = li[0]
    for i in range(len(li) - 1):
        li[i] = li[i + 1]
    li[-1] = first_element
    
    return li

if __name__ == "__main__":
    # Driver function
    numbers = [1, 2, 3, 4, 5]
    rotated_array = left_rotate_array(numbers)
    print(f"The rotated array is: {rotated_array}")