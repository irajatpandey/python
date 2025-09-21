def isIsomorphic(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_to_t_map = {}
    t_to_s_map = {}
    
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        
        # Condition 1: Check s_to_t mapping
        if char_s in s_to_t_map:
            if s_to_t_map[char_s] != char_t:
                return False
        
        # Condition 2: Check t_to_s mapping
        if char_t in t_to_s_map:
            if t_to_s_map[char_t] != char_s:
                return False
        
        # If both characters are new, create the mappings
        s_to_t_map[char_s] = char_t
        t_to_s_map[char_t] = char_s
        
    return True

if __name__ == "__main__":
    s1, t1 = "egg", "add"
    s2, t2 = "foo", "bar"
    print(f"Are '{s1}' and '{t1}' isomorphic? {is_isomorphic(s1, t1)}")
    print(f"Are '{s2}' and '{t2}' isomorphic? {is_isomorphic(s2, t2)}")