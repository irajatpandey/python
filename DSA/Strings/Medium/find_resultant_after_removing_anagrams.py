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
    
    result = [words[0]] # Start with the first word
    
    for i in range(1, len(words)):
        current_word = words[i]
        last_word_in_result = result[-1]
        
        # Compare current word with the last word added to the result list
        if not isAnagram(current_word, last_word_in_result):
            result.append(current_word)
            
    return result

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

