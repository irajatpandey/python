from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals in a list.
    """
    pass

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
    print(f"Merged intervals: {result}")