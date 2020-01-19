#examples from book

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])
message = "\nMy first bicycle was a " + bicycles[0].title() + "."

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
#changes the value of the first item to 'ducati
#motorcycles[0] = 'ducati' 
#print(motorcycles)
'''
When you append an item to a list,
the new element is added to the end of the list. 
Using the same list we had in the previous example, 
we’ll add the new element 'ducati' to the end of the list:
'''
motorcycles.append('ducati') 
print(motorcycles)

'''
The append() method makes it easy to build lists dynamically. 
For example, you can start with an empty list and then add items 
to the list using a series of append() statements. 
'''
my_motorcycles = []
my_motorcycles.append('honda')
my_motorcycles.append('yamaha')
my_motorcycles.append('suzuki')
print(my_motorcycles)
'''
can add a new element at any position in your 
list by using the insert() method. 
You do this by specifying the index 
of the new element and the value of the new item.
'''
my_motorcycles.insert(0, 'ducati') 
print(my_motorcycles)

#Can remove an item according to its position 
#in the list or according to its value.
# use del statement

del my_motorcycles[0] 
print(my_motorcycles)

'''
The pop() method removes the last item in a list, 
but it lets you work with that item after removing it. 
The term pop comes from thinking of a list as a stack of 
items and popping one item off the top of the stack. In this analogy, 
the top of a stack corresponds to the end of a list.
'''
#motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)
   
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

'''
Can actually use pop() to remove an item in a list at 
any position by including the index of the item 
you want to remove in parentheses.
'''
first_owned = my_motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

'''
Sometimes you won’t know the position of the value you 
want to remove from a list. If you only know the value 
of the item you want to remove,
 you can use the remove() method.
'''

print(motorcycles)
motorcycles.remove('ducati') 
print(motorcycles)

too_expensive = 'ducati'
my_motorcycles.remove(too_expensive)
print(my_motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

'''
The remove() method deletes only the first occurrence 
of the value you specify. If there’s a possibility the 
value appears more than once in the list, you’ll need to 
use a loop to determine 
if all occurrences of the value have been removed.
'''

        