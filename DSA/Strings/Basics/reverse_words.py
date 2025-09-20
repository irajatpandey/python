# reverse_words.py

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        # Your provided implementation
        def strip_spaces(s: str) -> List[str]:
            char_list = []
            i = 0
            n = len(s)
            while i < n and s[i] == ' ':
                i += 1
            while i < n:
                if s[i] != ' ':
                    char_list.append(s[i])
                elif char_list and char_list[-1] != ' ':
                    char_list.append(' ')
                i += 1
            if char_list and char_list[-1] == ' ':
                char_list.pop()
            return char_list

        def reverse_sub_array(char_list: List[str], start: int, end: int):
            while start < end:
                char_list[start], char_list[end] = char_list[end], char_list[start]
                start += 1
                end -= 1

        char_list = strip_spaces(s)
        n = len(char_list)
        reverse_sub_array(char_list, 0, n - 1)

        start = 0
        for i in range(n):
            if char_list[i] == ' ':
                reverse_sub_array(char_list, start, i - 1)
                start = i + 1
            elif i == n - 1:
                reverse_sub_array(char_list, start, i)

        return "".join(char_list)

if __name__ == "__main__":
    tests = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "Alice does not even like bob"
    ]
    sol = Solution()
    for t in tests:
        print(f"in : {repr(t)}")
        print(f"out: {sol.reverseWords(t)}")
