# freq_sort.py

class Solution:
    def frequencySort(self, s: str) -> str:
        # TODO: implement
        return ""

if __name__ == "__main__":
    sol = Solution()
    tests = [
        "tree",
        "cccaaa",
        "Aabb",
        ""
    ]
    for t in tests:
        print(f"in : {repr(t)}")  # [web:80][web:93]
        print(f"out: {sol.frequencySort(t)}")  # [web:80][web:93]
