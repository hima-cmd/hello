'''
Deli: Make a list called sandwich_orders and 
fill it with the names of various sandwiches . 
Then make an empty list called finished_sandwiches . 
Loop through the list of sandwich orders and print a 
message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches .
After all the sandwiches have been made, print a message listing 
each sandwich that was made .
'''


sandwich_orders =['pastrami','cheese','tuna','egg','pastrami','bacon',
                  'chicken','humus','pastrami']
finished_sandwiches =[]

types_sandwiches = len(sandwich_orders)
print("\nDifferent type of sandwiches : "+str(types_sandwiches))
print("\nDeli has run out of 'Pastrami',Sorry !!!!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\nSandwiches available : ")
print(sandwich_orders)

types_sandwiches = len(sandwich_orders)
print("\nDifferent type of sandwiches : "+str(types_sandwiches))

while types_sandwiches !=0:
    order_name = sandwich_orders.pop()
    print("\nPreparing your "+order_name+" sandwich.")
    finished_sandwiches.append(order_name)
    types_sandwiches = types_sandwiches -1
print("===============\n")        
for name in finished_sandwiches:
    print("\nPrepared "+name+" sandwich.")
    
print("\nOrders left : "+str(len(sandwich_orders)))
print(sandwich_orders)

'''
No Pastrami: Using the list sandwich_orders , 
make sure the sandwich 'pastrami' appears in the 
list atleast three times . Add code near the beginning 
of your program to print a message saying the deli 
has run out of pastrami, and then use a while loop 
to remove all occurrences of 'pastrami' from sandwich_orders . 
Make sure no pastrami sandwiches end up in finished_sandwiches .
'''