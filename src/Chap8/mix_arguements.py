'''Mixing Positional and Arbitrary Arguments
If you want a function to accept several different kinds of 
arguments, the parameter that accepts an arbitrary number of 
arguments must be placed last in the function definition. 
Python matches positional and keyword arguments first and 
then collects any remaining arguments in the final parameter.'''

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(size = 6)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing 
    everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print("\nUsing Arbitary keyword Arguements.")
print(user_profile)


