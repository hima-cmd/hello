# working with tuples

food_list =('bread','eggs','juice','coffee','fruit')
print("Food list : ")
for item in food_list:
    print(item)

#can't do this   
#food_list[3] = 'tea'

food_list = ('bread','eggs','juice','tea','custard')
print("overwritten Food list : ")
for item in food_list:
    print(item)
    