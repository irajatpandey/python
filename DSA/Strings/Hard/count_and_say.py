# count_and_say.py

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        smallOutput = self.countAndSay(n - 1)
        i = 1
        count = 1  # Count 1 se shuru hoga
        ans = ""
        
        while i < len(smallOutput):
            if smallOutput[i] == smallOutput[i-1]:
                count += 1
            else:
                ans = ans + str(count) + smallOutput[i-1] # Pichle group ko add karo
                count = 1  # Naye group ke liye count reset
            i += 1
        ans = ans + str(count) + smallOutput[i-1]
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [1, 2, 3, 4, 5, 6]
    for n in tests:
        print(f"in : {n}")  # [web:108][web:114]
        print(f"out: {sol.countAndSay(n)}")  # [web:108][web:114]
