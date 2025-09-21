# 2273. Find Resultant Array After Removing Anagrams
# File: find_resultant_after_removing_anagrams.py

from typing import List
def isAnagram(s1 : str, s2: str) -> bool:
    mapp = {}
    if len(s1) != len(s2):
        return False

    for char in s1:
        mapp[char] = mapp.get(char, 0) + 1
    for char in s2:
        mapp[char] = mapp.get(char, 0) - 1
    
    for value in mapp.values():
        if value != 0:
            return False
        
    return True
def removeAnagrams(words: List[str]) -> List[str]:  

    
    if not words:
        return []
    
    n = len(words)
    i = 1
    s3 = words[0]

    while i < len(words):
        if isAnagram(s3, words[i]):
            words.pop(i)
        else:
            s3 = words[i]
            i += 1
    return words

def run_tests():
    tests = [
        (["abba","baba","bbaa","cd","cd"], ["abba","cd"]),
        (["a","b","c","d","e"], ["a","b","c","d","e"]),
        ([], []),
        (["abc","bca","cab"], ["abc"]),
        (["cd","cd","cd"], ["cd"]),
    ]
    passed = 0
    for i, (inp, exp) in enumerate(tests, 1):
        # Create a copy of the input list for each test
        list_copy = inp[:]
        try:
            got = removeAnagrams(list_copy)
        except NotImplementedError as e:
            print(f"Test {i}: SKIPPED -> {e}")
            continue
        ok = got == exp
        print(f"Test {i}: {'OK' if ok else 'FAIL'} | in={inp} exp={exp} got={got}")
        passed += ok
    print(f"Passed {passed}/{len(tests)} tests")

if __name__ == "__main__":
    run_tests()

