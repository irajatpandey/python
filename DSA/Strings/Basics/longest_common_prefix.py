from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.
    """
    pass

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    print(f"Longest common prefix for {strs1}: '{longest_common_prefix(strs1)}'")
    print(f"Longest common prefix for {strs2}: '{longest_common_prefix(strs2)}'")