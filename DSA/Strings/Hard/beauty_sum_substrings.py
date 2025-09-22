# beauty_sum_substrings.py

class Solution:
    def beautySum(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1   
                count += max(freq.values()) - min(freq.values())

        return count

if __name__ == "__main__":
    sol = Solution()
    tests = ["aabcb", "abaacc", "abc", "zzz"]
    for t in tests:
        print(f"in : {t}")  # [web:111][web:105]
        print(f"out: {sol.beautySum(t)}")  # [web:111][web:105]
