# longest_pal_substring.py

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # TODO: implement (e.g., expand around centers)
        return ""

if __name__ == "__main__":
    sol = Solution()
    tests = ["babad", "cbbd", "a", "ac", "forgeeksskeegfor"]
    for t in tests:
        print(f"in : {t}")  # [web:102][web:100]
        print(f"out: {sol.longestPalindrome(t)}")  # [web:102][web:100]
