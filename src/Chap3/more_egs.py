#more examples from book
'''
sort() method makes it relatively easy to sort a list.
The sort() method, changes the order of the list permanently. 
The cars are now in alphabetical order, 
and we can never revert to the original order:
'''
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort()
print(cars)

#can also sort this list in reverse alphabetical order by 
#passing the argument reverse=True to the sort() method.
cars.sort(reverse=True)
print(cars)

'''
To maintain the original order of a list but 
present it in a sorted order, you can use the sorted() function.
The sorted() function lets you display your list in a particular order
but doesn’t affect the actual order of the list.
'''

print("Here is the original list:") 
print(cars)
print("\nHere is the sorted list:") 
print(sorted(cars))
print("\nHere is the original list again:") 
print(cars)
cars.reverse()
print(cars)