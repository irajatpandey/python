# Loop on list

li = [1, 2, 3, "apple", 12.22]

for i in range(len(li)):
    print(li[i], end = " ")

for ele in li:
    print(ele, end = " ")

#slicing
for ele in li[2:]:
    print(ele)
