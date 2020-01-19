#dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title()) 
    print("\tLocation: " + location.title())
    
# more examples of nesting
# nesting dictionary in a list

person_info_1 = {
    'first_name' : 'rajit',
    'last_name' :'suggula',
    'age' : 40,
    'city' :'sutton',
    }

person_info_2 = {
    'first_name' : 'abhi',
    'last_name' :'suggula',
    'age' : 7,
    'city' :'sutton',
    }

person_info_3 = {
    'first_name' : 'anvi',
    'last_name' :'suggula',
    'age' : 3,
    'city' :'sutton',
    }

person_list = [person_info_1 , person_info_2 , person_info_3]

for info in person_list:
    print('\nFirst name : '+info['first_name'])
    print('Last name : '+info['last_name'])
    print('Age : '+str(info['age']))
    print('City : '+info['city'])    

