
def reverse( nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

def rotate(nums: list, k: int) -> None:
    n = len(nums)
    # Handle cases where k > n
    k = k % n
    if k == 0 or n <= 1:
        return

    # Step 1: Reverse first n-k elements
    reverse(nums, 0, n - k - 1)

    # Step 2: Reverse remaining k elements
    reverse(nums, n - k, n - 1)

    # Step 3: Reverse the whole list
    reverse(nums, 0, n - 1)

if __name__ == "__main__":
    # Example data
    nums = [1, 2, 3, 4, 5]
    d = 2
    
    # Yahaan aapka function call hoga
    rotate(nums, d)
    print(f"The rotated array is: {nums}")