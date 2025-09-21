# max_depth_parentheses.py

class Solution:
    def maxDepth(self, s: str) -> int:
        # TODO: implement
        return 0

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "(1+(2*3)+((8)/4))+1",
        "(1)+((2))+(((3)))",
        "()(())((()))",
        ""
    ]
    for t in tests:
        print(f"in : {repr(t)}")  # [web:88][web:85]
        print(f"out: {sol.maxDepth(t)}")  # [web:88][web:85]
