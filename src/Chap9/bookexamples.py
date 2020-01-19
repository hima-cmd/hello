class Dog():
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command.""" 
        print(self.name.title() + " is now sitting.")
       
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
           

'''in python 2.7
class ClassName(object): --snip--
class Dog(Object): 
'''
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()

'''------------Next Example--------------'''
class Restaurants():
    """Class Restaurant with info - name & cuisine."""
    def __init__(self,name,cuisine):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
    
    """ Methods to work with the attributes."""
    def describe_restaurant(self):
        """Display the attributes of the object"""
        print("\nThe Restaurant is : "+self.name.title()+
              "\nand the Cuisine is : "+self.cuisine.title())
    
    def open_restaurant(self):
        """Display restaurant is open."""
        print("Restaurant : "+self.name.title()+" is open.")

'''Creating instances of class Restaurant.'''
restaurant_jimmy = Restaurants('jimmy','multi')
restaurant_roshni = Restaurants('roshni','indian')
restaurant_chennai = Restaurants('chennai dosa','south indian')

'''Displaying information about restaurants.'''
restaurant_jimmy.describe_restaurant()
restaurant_jimmy.open_restaurant()

restaurant_roshni.describe_restaurant()
restaurant_roshni.open_restaurant()

restaurant_chennai.describe_restaurant()
restaurant_chennai.open_restaurant()
