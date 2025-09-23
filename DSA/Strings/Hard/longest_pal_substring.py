# longest_pal_substring.py

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome found
            return s[left + 1 : right]
        
        if len(s) <= 1:
            return s
            
        longest = ""
        
        for i in range(len(s)):
            # Odd length palindrome
            odd_palindrome = expand_from_center(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            
            # Even length palindrome
            even_palindrome = expand_from_center(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
                
        return longest

if __name__ == "__main__":
    sol = Solution()
    tests = ["babad", "cbbd", "a", "ac", "forgeeksskeegfor"]
    for t in tests:
        print(f"in : {t}") 
        print(f"out: {sol.longestPalindrome(t)}")