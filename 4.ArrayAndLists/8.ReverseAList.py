def reverseList(li):
    length = len(li)
    for i in range(length // 2):
        li[i], li[length - i - 1] = li[length - i - 1], li[i]
    return

li = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
print(li)

reverseList(li)
print(li)

## Reverse a List in one line

li = li[::-1]
print(li)