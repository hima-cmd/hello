alien_color = 'green'

if alien_color != 'yellow' and alien_color != 'red':
    print('player just earned 5 points.')
elif (alien_color != 'red') and (alien_color != 'green'):
    print('\nplayer just earned 10 points.')
else:
    print('\nplayer just earned 15 points.')

#Stages of Life

# Checking that a List is not Empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".") 
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
   
   