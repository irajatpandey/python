# freq_sort.py

class Solution:
    def frequencySort(self, s: str) -> str:
        map1 = {}
        for char in s:
            map1[char] = map1.get(char, 0) + 1
        sorted_items = sorted(map1.items(), key=lambda item: item[1],reverse=True)
        sorted_dict = dict(sorted_items)
        output = ""
        for key, value in sorted_dict.items():
            output += key * value
        return output

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
