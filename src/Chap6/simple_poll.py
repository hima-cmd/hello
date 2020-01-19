favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
print("Sarah's favorite language is " + 
      favorite_languages['sarah'].title() + 
      ".\n")

for name, language in favorite_languages.items():
    print(name.title() + 
          "'s favorite language is " +
        language.title() + ".")

#for name in favorite_languages: also means ==
for name in favorite_languages.keys():
    print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
       print(name.title())
       if name in friends:
           print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
 
if 'erin' not in favorite_languages.keys(): 
    print("Erin, please take our poll!")
    
#sorted() function to get a copy of the keys in order:
for name in sorted(favorite_languages.keys()):
       print(name.title() + ", thank you for taking the poll.")
       
       
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
print("====\n")
    
# to print only unique set of values , use set
for language in set(favorite_languages.values()): 
    print(language.title())

print("====\n")



# dictionary about person
person_info = {
    'first_name' : 'rajit',
    'last_name' : ' suggula',
    'age' : 40,
    'city' : 'sutton',
    'fav_num' : 1, 
    }

print(person_info)
print('Name :' + person_info['first_name'])


#looping through dictionaries

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items(): 
    print("\nKey: " + key)
    print("Value: " + value)


