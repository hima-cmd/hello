#using while , break , continue and flag
toppings =''
active = True

while active:
    toppings = raw_input("\nEnter toppings of your choice : ")
    if toppings != 'quit':   
        print('\n Adding '+toppings+' to your pizza.......')
    else:
        print("\nThank you for your order.")
        active = False
        # or add break
        

