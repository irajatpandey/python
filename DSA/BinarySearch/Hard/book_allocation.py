from typing import List

class Solution:
    def findPages(self, arr: List[int], k: int) -> int:
        """
        Finds the minimum value of the maximum number of pages assigned to any student 
        when allocating books (represented by pages in arr) to k students.
        
        Args:
            arr (List[int]): List of page counts for each book.
            k (int): The number of students available.

        Returns:
            int: The minimum possible maximum page count, or -1 if allocation is not possible.
        """
        
        # --- 1. Edge Case Check ---
        # If the number of students (k) is greater than the number of books, 
        # allocation is not possible as some students will get no book.
        if k > len(arr):
            return -1
        
        def check(arr: List[int], k: int, max_pages: int) -> bool:
            """
            Feasibility function: Checks if books can be allocated such that 
            no student exceeds the 'max_pages' limit, using K or fewer students.
            """
            students_needed = 1  # Start with the first student
            current_pages = 0
            
            for page in arr:
                # If adding the current book exceeds the maximum page limit for the current student
                if current_pages + page > max_pages:
                    # Start a new student
                    students_needed += 1
                    current_pages = page  # New student starts with the current book
                else:
                    # Current student takes the book
                    current_pages += page
            
            # The allocation is possible if the students needed do not exceed the limit k.
            return students_needed <= k

        # --- 2. Define Search Space ---
        # Start (Lower Bound): The smallest possible answer is the largest single book.
        start = max(arr) 
        # End (Upper Bound): The largest possible answer is the total sum of all books.
        end = sum(arr)
        
        # 'ans' stores the smallest valid max_pages limit found so far.
        ans = -1 
        
        # --- 3. Binary Search Execution ---
        while start <= end:
            mid = start + (end - start) // 2  # The current potential max_pages limit
            
            # Check feasibility with the current limit (mid)
            if check(arr, k, mid):
                # If feasible: 'mid' works. Store it and try to find an even smaller limit (search left).
                ans = mid
                end = mid - 1
            else:
                # If not feasible: 'mid' is too small; we need a larger limit (search right).
                start = mid + 1
                
        # 'ans' holds the minimum maximum page count required.
        return ans

if __name__ == "__main__":
    s = Solution()
    test_cases = [
        # (pages, students, expected_min_max_pages)
        ([12, 34, 67, 90], 2, 113),  # Allocation: [12, 34, 67] (113) | [90] (90). Max is 113.
        ([10, 20, 30, 40], 2, 60),   # Allocation: [10, 20, 30] (60) | [40] (40). Max is 60.
        ([25, 46, 75, 12, 35], 3, 75), # Allocation: [25, 46] (71) | [75] (75) | [12, 35] (47). Max is 75.
        ([10, 20, 30], 4, -1)        # Edge Case: k > books. Should return -1.
    ]
    
    print("--- Book Allocation Problem (Minimize Maximum Pages) ---")
    for arr, k, expected in test_cases:
        result = s.findPages(arr, k)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Books: {arr}, Students: {k}")
        print(f"  Expected Min Max Pages: {expected}, Got: {result} ({status})")
    print("-" * 60)