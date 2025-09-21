# implement_atoi.py

class Solution:
    def myAtoi(self, s: str) -> int:
        # TODO: implement
        return 0

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
