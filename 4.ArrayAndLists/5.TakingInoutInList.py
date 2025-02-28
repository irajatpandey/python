#LineSeparated Input

size = int(input())
li = []
for i in range(size):
    x = int(input())
    li.append(x)

print(li)

# Space Separated Input
li = [int(x) for x in input().split()]
print(li)