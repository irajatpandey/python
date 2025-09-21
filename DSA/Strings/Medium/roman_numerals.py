# roman_numerals.py

class Solution:
    def romanToInt(self, s: str) -> int:
        # TODO: implement
        return 0

    def intToRoman(self, num: int) -> str:
        # TODO: implement
        return ""

if __name__ == "__main__":
    sol = Solution()
    roman_tests = ["III", "LVIII", "MCMXCIV", "IX"]
    int_tests = [3, 58, 1994, 9]
    for r in roman_tests:
        print(f"romanToInt in : {r}")  # [web:95][web:89]
        print(f"romanToInt out: {sol.romanToInt(r)}")  # [web:95][web:89]
    for n in int_tests:
        print(f"intToRoman in : {n}")  # [web:86][web:95]
        print(f"intToRoman out: {sol.intToRoman(n)}")  # [web:86][web:95]
