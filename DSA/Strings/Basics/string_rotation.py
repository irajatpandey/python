def check_substring(final_string: str, goal: str) -> bool:
    len_final = len(final_string)
    len_goal = len(goal)

    # Outer loop for all possible starting positions in the final_string
    for i in range(len_final - len_goal + 1):
        is_match = True
        
        # Inner loop to compare the characters
        for j in range(len_goal):
            if final_string[i + j] != goal[j]:
                is_match = False
                break
        
        if is_match:
            return True
    
    return False
def is_rotation(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    final_string = s + s   
    if check_substring(final_string, goal):
        return True
    return False
  

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"
    s3 = "hello"
    print(f"Is '{s2}' a rotation of '{s1}'? {is_rotation(s1, s2)}")
    print(f"Is '{s3}' a rotation of '{s1}'? {is_rotation(s1, s3)}")