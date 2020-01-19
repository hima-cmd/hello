# 
pizzas_list = ['veggie','chicken','spicy veggie']
print('Original pizza list : ')
print(pizzas_list)
friend_pizzas = pizzas_list[:]

pizzas_list.append('bbq')
friend_pizzas.append('tuna')

print("My favourites :")
for item in pizzas_list:
    print(item)

print("My friends favourites :")
for item in friend_pizzas:
    print(item)