# reverse_every_word.py

class Solution:
    def reverseWords(self, s: str) -> str:
        # TODO: implement (reverse each word’s characters, keep word order)
        return ""

if __name__ == "__main__":
    sol = Solution()
    tests = ["Let's code", "the sky is blue", " hello  world "]
    for t in tests:
        print(f"in : {repr(t)}")  # [web:106][web:118]
        print(f"out: {sol.reverseWords(t)}")  # [web:106][web:118]
