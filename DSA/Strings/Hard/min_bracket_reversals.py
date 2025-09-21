# min_bracket_reversals.py

class Solution:
    def countMinReversals(self, s: str) -> int:
        # TODO: implement
        return 0

if __name__ == "__main__":
    sol = Solution()
    tests = ["}{", "{{{", "{{{{}}", "}{{}}{{{", "{{{{}}}}", "{{}}}}{"]  # mixed samples
    for t in tests:
        print(f"in : {t}")  # [web:119][web:107]
        print(f"out: {sol.countMinReversals(t)}")  # [web:119][web:107]
