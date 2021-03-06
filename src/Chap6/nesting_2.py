# Store information about a pizza being ordered. 

# List inside a dictionary

pizza = {
       'crust': 'thick',
       'toppings': ['mushrooms', 'extra cheese'],
       }

# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
                "with the following toppings:")
for topping in pizza['toppings']: 
    print("\t" + topping)
    
#more than one value to be associated with a single key in a dictionary.
favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages: 
        print("\t" + language.title())
        

