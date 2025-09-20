from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals in a list.
    """
    intervals.sort()
    output = []
    output.append(intervals[0])

    for i in range(1, len(intervals)):
        last_merged = output[-1]
        current_interval = intervals[i]

        if current_interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            output.append(current_interval)
    return output

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
    print(f"Merged intervals: {result}")