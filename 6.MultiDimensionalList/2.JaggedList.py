# Jagged List

# A jagged array is an array of arrays such that member arrays can be of different sizes, i.e., 
#we can create a 2-D array but with a variable number of columns in each row. These types of arrays are also known as Jagged arrays. 

li = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]

for i in li:
    for j in i:
        print(j, end = " ")
    print()
    
# output - 1 2 3 4 
#          5 6 7
#          8 9