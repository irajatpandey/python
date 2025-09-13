def is_array_sorted(li: list) -> bool:
    # Handle edge cases (empty or single-element list is always sorted)
    if len(li) <= 1:
        return True

    # 1. Check if the array is sorted in non-decreasing (ascending) order
    is_ascending = True
    for i in range(len(li) - 1):
        if li[i] > li[i + 1]:
            is_ascending = False
            break

    # 2. Agar ascending nahi hai, to check karein ki kya descending hai
    is_descending = True
    if not is_ascending:
        for i in range(len(li) - 1):
            if li[i] < li[i + 1]:
                is_descending = False
                break
        
    return is_ascending or is_descending


if __name__ == "__main__":
    sorted_array = [1, 2, 3, 4, 5]
    unsorted_array = [10, 5, 20, 15]

    print(f"Is {sorted_array} sorted? {is_array_sorted(sorted_array)}")
    print(f"Is {unsorted_array} sorted? {is_array_sorted(unsorted_array)}")