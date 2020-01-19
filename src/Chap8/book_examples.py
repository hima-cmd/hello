'''A function call tells Python to execute the code in the function.
 To call a function, you write the name of the function, 
 followed by any necessary information in parentheses. 
 Because no information is needed here, calling our function 
is as simple as entering greet_user().

'''

def greet_user(username):
    """Display a simple greeting."""
    print("Hello!") 
    print("Hello, " + username.title() + "!")
    
greet_user('rajit')
'''
The variable username in the definition of greet_user()
is an example of a parameter, a piece of information 
the function needs to do its job. 
The value 'jesse' in greet_user('jesse') is an example of an argument. 
An argument is a piece of information that is passed from a function call 
to a function.
'''
""" Examples to try """

def display_message():
    print('\nhello , reading new book.')

display_message()

def fav_book(book_name):
    print("\nMy favourite book is "+book_name+".")

fav_book('harry potter')

'''Example about positional arguements'''
''' in the function call, the argument 'hamster' is stored in 
the parameter animal_type and 
the argument 'harry' is stored in the parameter pet_name
'''

def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

