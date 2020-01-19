#show_magicians() function to display magician name.
def show_magicians(mag_name):
    #Print the name of magician in the list.
    for name in mag_name:
        print("\nMagician name : "+name.title())

#make_great() function to modify the name of magician
def make_great(mag_name):
    #For saving the modified magicians name
    great_magicians_list =[]
    #Till there is atleast one name in the magicians name list
    while mag_name:
        #Get name , modify and add to new list of great_magicians
        magician_name = mag_name.pop()
        magician_name = "The Great " + magician_name
        great_magicians_list.append(magician_name)
    #Return the list with modified name of magicians    
    return great_magicians_list

#Create a list of magician names
magicians_list = ['oliver','jamie','ruby','sally','sam']
#Pass the list to display the magician's name.
show_magicians(magicians_list)

#Modify the name of the magicians
#great_magicians = make_great(magicians_list)
#Pass the list of modified magicians name to display.
#print('\nThe Original Magician Name List : ')
#show_magicians(magicians_list)
#print('\nThe Modified Magician Name List : ')
#show_magicians(great_magicians)

#To save a copy of the original name list, 
#pass copy of original list magician_list
great_magicians = make_great(magicians_list[:])
#Pass the list of modified magicians name to display.
print('\nThe Original Magician Name List : ')
show_magicians(magicians_list)
print('\nThe Modified Magician Name List : ')
show_magicians(great_magicians) 
