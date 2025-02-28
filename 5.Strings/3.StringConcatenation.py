str = "red"
print(id(str)) #outut - 2151194316720

str = str + "green"
print(id(str)) #output - 2151196360112

print(str) #output - redgreen

# another use case

str = str * 3
print(str) #output - redgreenredgreenredgreen