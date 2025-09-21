# roman_numerals.py

class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        output = 0
        n = len(s)
        for i in range(n - 1):
            current_char = mapp[s[i]]
            next_char = mapp[s[i + 1]]

            if current_char < next_char:
                output -= current_char
            else:
                output += current_char
        output += mapp[s[n - 1]]
        return output
        


if __name__ == "__main__":
    sol = Solution()
    roman_tests = ["III", "LVIII", "MCMXCIV", "IX"]
    int_tests = [3, 58, 1994, 9]
    for r in roman_tests:
        print(f"romanToInt in : {r}")  # [web:95][web:89]
        print(f"romanToInt out: {sol.romanToInt(r)}")  # [web:95][web:89]
