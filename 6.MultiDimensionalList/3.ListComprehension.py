 # List Comprehension
li = [1, 2, 3, 4]
 
# find the square of each element and store it into a new list
new_list = [ele ** 2 for ele in li] 
print(new_list) #output - [1, 4, 9, 16]

#find the square of even numbers only

new_even_square = [ele ** 2 for ele in li if ele % 2 == 0]
print(new_even_square) #[4, 16]

#Find the common elements between two list
l1 = [1, 2, 3, 4, 5]
l2 = [2, 4, 6, 7]

common_element = [ele for ele in l1 for ele2 in l2 if ele == ele2]
print(common_element) # output - [2, 4]

#List within a list
li = ["India", "London", "Zurich"]
list_2d = [[c for c in ele] for ele in li]
print(list_2d) # [['I', 'n', 'd', 'i', 'a'], 
               #  ['L', 'o', 'n', 'd', 'o', 'n'], 
               #  ['Z', 'u', 'r', 'i', 'c', 'h']] 