#counting to twenty
print("range(1,21) : ")
for num in range(1,21):
    print(num)
    
for value in range(1,5):
    print(value)
    
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
#working on million
no_list = []
for no in range(1,1000000):
    no_list.append(no)
    #print(no)

print("min in no_list : "+str(min(no_list)))
print("max in no_list : "+str(max(no_list)))
print("sum of all nos in no_list : "+str(sum(no_list)))

 #odd numbers list
odd_list = list(range(1,20,2))
print(" odd numbers in range(1,20) : ")
for odd in odd_list:
    print(odd)

#threes
mult_three = list(range(3,31,3))
print("multiples of 3 : ")
for num in mult_three:
    print(num)
     
#cubes
# cubes_list =[]
# for value in range(1,10):
#     cubes_list.append(value**3)

cubes_list = [value**3 for value in range(1,10)]
print("cubes list : ")
for num in cubes_list:
    print(num)
    
    
squares = []
for value in range(1,11): 
    square = value**2
squares.append(square)

#for value in range(1,11):
#    squares.append(value**2)
print(squares)

list_squares = [value**2 for value in range(1,11)]
print(list_squares)