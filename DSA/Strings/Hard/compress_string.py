from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read_ptr = 0
        write_ptr = 0
        n = len(chars)

        while read_ptr < n:
            current_char = chars[read_ptr]
            count = 0
            while read_ptr < n and chars[read_ptr] == current_char:
                read_ptr += 1
                count += 1
            chars[write_ptr] = current_char
            write_ptr += 1
            if count > 1:
                for digit in str(count):
                    chars[write_ptr] = digit
                    write_ptr += 1
        return write_ptr


def main():
    s = Solution()

    test_cases = [
        (['a', 'a', 'b', 'b', 'c', 'c', 'c'], 6, ['a', '2', 'b', '2', 'c', '3']),
        (['a'], 1, ['a']),
        (['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], 4, ['a', 'b', '1', '1']),
        (['a', 'a', 'a'], 2, ['a', '3']),
        (['a', 'a', 'b', 'b'], 4, ['a', '2', 'b', '2'])
    ]

    print("Running tests for compress function...\n")

    for i, (input_list, expected_len, expected_list) in enumerate(test_cases, 1):
        # Create a copy to prevent in-place modification from affecting other tests
        chars_copy = input_list[:]
        
        # Call the function and get the new length
        new_len = s.compress(chars_copy)
        
        # Get the compressed part of the list
        got_list = chars_copy[:new_len]
        
        ok = new_len == expected_len and got_list == expected_list
        status = "PASS ✅" if ok else "FAIL ❌"
        
        print(f"Test {i}: {status}")
        print(f"  Input:    {input_list}")
        print(f"  Expected: {expected_list}, Length: {expected_len}")
        print(f"  Got:      {got_list}, Length: {new_len}\n")

if __name__ == "__main__":
    main()