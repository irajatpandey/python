# Replace Character in Strings
def replaceCharacterInString(str, char1, char2):
    ans = ""
    for i in range(len(str)):
        if str[i] == char1:
            ans += char2
        else:
            ans += str[i]
    return ans

str = "abbcdb"
print(replaceCharacterInString(str, 'b', 'z'))
print(str.replace('b', 'z'))

