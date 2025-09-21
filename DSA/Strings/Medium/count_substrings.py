# count_substrings.py

class Solution:
    def countSubstrings(self, s: str) -> int:
        # TODO: implement
        return 0

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "abc",
        "aaa",
        "",
        "ababa"
    ]
    for t in tests:
        print(f"in : {repr(t)}")  # [web:66][web:90]
        print(f"out: {sol.countSubstrings(t)}")  # [web:66][web:90]
