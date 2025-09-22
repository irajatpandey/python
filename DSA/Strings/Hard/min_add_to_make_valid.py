class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        balance = 0
        moves = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                moves += 1
                balance = 0
        
        moves += balance
        
        return moves

def main():
    s = Solution()
    
    test_cases = [
        ("())", 1),
        ("(((", 3),
        ("()", 0),
        (")(", 2),
        ("", 0),
        ("()()", 0),
        ("())(", 2)
    ]
    
    print("Running tests for minAddToMakeValid...\n")
    
    for input_str, expected_output in test_cases:
        actual_output = s.minAddToMakeValid(input_str)
        print(f"Input: '{input_str}'")
        print(f"Expected: {expected_output}")
        print(f"Got: {actual_output}")
        if actual_output == expected_output:
            print("Status: PASS ✅\n")
        else:
            print("Status: FAIL ❌\n")

if __name__ == "__main__":
    main()