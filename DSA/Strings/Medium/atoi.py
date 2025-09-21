# implement_atoi.py
import math
class Solution:
    # def remove_spaces(self, s : str) -> None:
    #     i = 0
    #     n = len(s)
    #     s
    #     while i < n and s[i] == ' ' or s[i] == '-' or s[i] == '+':
    #           i += 1
    #     j = n - 1

    #     while j >= 0 and s[j] == ' ' or not s[j].isdigit():
    #         j -= 1
    #     return s[i : j + 1]


    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        sign = 1
        output = 0

        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:     ## testcase s = " ", output : 0
            return 0
        
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])
            output = output * 10 + digit
            i += 1
        
        output = output * sign
        max_int = int(math.pow(2, 31)) - 1
        min_int = int(-math.pow(2, 31))
        
        if output > max_int:
            return max_int
        elif output < min_int:
            return min_int
        
        return output
        

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "+1",
        "   +0 123"
    ]
    for t in tests:
        print(f"in : {repr(t)}")  # [web:61][web:65]
        print(f"out: {sol.myAtoi(t)}")  # [web:61][web:65]
