'''A keyword argument is a name-value pair that you pass to a function. 
You directly associate the name and the value within the argument, 
Keyword arguments free you from having to worry about correctly ordering 
your arguments in the function call, 
and they clarify the role of each value in the function call. '''
"""When you use keyword arguments, be sure to use the exact names
of the parameters in the function's definition. When writing a function,
you can define a default value for each parameter. 
If an argument for a parameter is provided in the function call, 
Python uses the argument value. If not, it uses the parameters default value. 
So when you define a default value for a parameter, you can 
exclude the corresponding argument you usually write in the 
function call. Using default values can simplify your function calls
and clarify the ways in which your functions are typically used."""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type='hamster', pet_name='harry')

'''default values'''
def describe_pets(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pets(pet_name='willy')
describe_pets(pet_name='feather', animal_type='hamster')

#different ways to call a function
# A dog named sally.
describe_pets('sally')
describe_pets(pet_name='sally')
# A hamster named terry
describe_pets('terry', 'hamster')
describe_pets(pet_name='terry', animal_type='hamster')
describe_pets(animal_type='hamster', pet_name='terry')
