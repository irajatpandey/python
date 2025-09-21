from typing import List

from typing import List

def longest_common_prefix(strs: List[str]) -> str:
    # Handle the edge case where the list is empty.
    if not strs:
        return ""

    # Use the first string as our reference for character-by-character comparison.
    first_string = strs[0]

    # Iterate through the characters of the first string.
    # We use enumerate() to get both the index (i) and the character (char).
    for i, char in enumerate(first_string):
        
        # Now, compare this character with the same character
        # at the same position in all other strings.
        for j in range(1, len(strs)):
            
            # Check for two conditions:
            # 1. Is the current string too short? (i.e., its length is i or less)
            # 2. Do the characters at index i not match?
            if i >= len(strs[j]) or strs[j][i] != char:
                # If either condition is true, we have found our longest prefix.
                # We return the substring of the first string up to this index.
                return first_string[:i]

    # If the outer loop finishes without returning, it means the
    # entire first string is the common prefix.
    return first_string

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    print(f"Longest common prefix for {strs1}: '{longest_common_prefix(strs1)}'")
    print(f"Longest common prefix for {strs2}: '{longest_common_prefix(strs2)}'")