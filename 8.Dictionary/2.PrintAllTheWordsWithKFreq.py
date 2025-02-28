words = ["i","love","leetcode","i","love","coding"]
k = 2

my_map = {}

for ele in words:
    if ele in my_map:
        my_map[ele] += 1
    else:
        my_map[ele] = 1

for item in my_map.keys():
    if(my_map[item] == k):
        print(my_map[item])



#optimization
dict = {}
for w in words:
    dict[w] = dict.get(w, 0) + 1

print(dict)