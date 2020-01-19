#make_sandwich() accepts a list of items to be on sandwich.
def make_sandwich(*items):
   #Starting the sandwich 
   print("\nMaking the sandwich with : ")
   for item in items:
       #Items to be put on sandwich
       print(" - "+item)

#Place sandwich orders with different items inside.
make_sandwich('cheese')
make_sandwich('tomato','cucumber','onions','ketchup') 
make_sandwich('cheese','tomato','chicken','lettuce')

print('\n-------User profile------\n')
#make_profile() function to create a dictionary with user info.
def make_profile(first_name , last_name, **user_info):
    #Start building dictionary with arbitary arguments.
    #
    print('Building a user_profile dictionary.')
    user_profile = {}
    user_profile['first_name'] = first_name
    user_profile['last_name'] = last_name
    #if any key-value arguments have been passed , 
    #then add to dictionary.
    if user_info:
        for key , value in user_info.items():
            user_profile[key] = value
    #return the dictionary thus created.
    return user_profile

def display_user_profile(profile):
    #Display all the key:value for each user in user_profile dictionary.
    print('\nDisplaying User Profiles .........')
    for key,value in profile.items():
        print(key.title +"  :  "+ value.title)

user_info = make_profile('abhi', 'suggula',)
display_user_profile(user_info)

user_info = make_profile('anvi', 'suggula', age = '3', gender = 'female')
display_user_profile(user_info)
     
''' *************** '''


#function to create dictionary for cars
def create_car_dict(manufacturer_name , model_name , **details):
    #building the dictionary
    car_info = {}
    print('\n--------------------------\n')
    print('\nBuilding the car dictionary')
    #Need manufacturer name and model name to start dictionary.
    if manufacturer_name and model_name:
        car_info['manufacturer_name'] = manufacturer_name
        car_info['model_name'] = model_name
        for key , value in details.items():
            car_info[key] = value
            
        return car_info
    else:
       print('\n Manufacturers Name and Model '+
       'Name of car required to create car dictionary.')
    

#function to display car dictionary 
def display_car_dict(car_dict):
    print('\nDisplaying the car dictionary :')
    for key , value in car_dict.items():
        print('\n '+ key + ' : ' +str(value).title() )

#Call to the functions
car = create_car_dict('subaru', 'outback', color='blue', tow_package=True)    
display_car_dict(car)
        
        
        
        
        
        