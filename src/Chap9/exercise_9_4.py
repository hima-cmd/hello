class Restaurants():
    """Class Restaurant with info - name & cuisine."""
    def __init__(self,name,cuisine):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0
    
    """ Methods to work with the attributes."""
    def describe_restaurant(self):
        """Display the attributes of the object"""
        print("\nThe Restaurant is : "+self.name.title()+
              "\nand the Cuisine is : "+self.cuisine.title())
    
    def open_restaurant(self):
        """Display restaurant is open."""
        print("Restaurant : "+self.name.title()+" is open.")
        
    def set_number_served(self , served):
        """Set the number_served - number of customers served"""
        self.number_served = served
    
    def add_number_served(self , cust_numbers):
        """Add given number to number_served."""
        self.number_served += cust_numbers
        
    def display_number_served(self):
        """Display the number of customers served by restuarant."""
        print("\nCustomers served so far at : " +self.name
              +"  , are : "+str(self.number_served))
        
        
'''Creating instances of class Restaurant.'''
restaurant_jimmy = Restaurants('jimmy','multi')
restaurant_roshni = Restaurants('roshni','indian')
restaurant_chennai = Restaurants('chennai dosa','south indian')

'''Displaying information about restaurants.'''
restaurant_jimmy.describe_restaurant()
restaurant_jimmy.open_restaurant()
restaurant_jimmy.display_number_served()
restaurant_jimmy.set_number_served(100)
restaurant_jimmy.display_number_served()

restaurant_roshni.describe_restaurant()
restaurant_roshni.open_restaurant()
restaurant_roshni.set_number_served(200)
restaurant_roshni.display_number_served()

restaurant_chennai.describe_restaurant()
restaurant_chennai.open_restaurant()
restaurant_chennai.number_served = 500
restaurant_chennai.display_number_served()
restaurant_chennai.add_number_served(500)
restaurant_chennai.display_number_served()

