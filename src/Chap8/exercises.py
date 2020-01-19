#Write a function called make_shirt() that accepts a size and 
#the text of a message that should be printed on the shirt . 
#The function should print a sentence summarizing the size of the 
#shirt and the message printed on it .Call the function once using 
#positional arguments to make a shirt . Call the function a second 
#time using keyword arguments .

def make_shirt(size,message):
    print("\nSize of the shirt :  "+size)
    print("\nMessage printed on shirt : "+message)
#using positional arguments    
make_shirt('large', 'position args')
#using keyword arguments
make_shirt( size = 'small', message ='hiya')

'''
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python . 
Make a large shirt and a medium shirt with the default message, 
and a shirt of any size with a different message .
'''

def make_shirts(size='large',message='i luv python'):
    print('\nSize of the shirt : ' +size)
    print('Message on the shirt : '+message)

make_shirts()
make_shirts('medium')
make_shirts('small', 'hello')


'''Write a function called describe_city() that accepts 
the name of a city and its country . 
The function should print a simple sentence, 
such as Reykjavik is in Iceland . 
Give the parameter for the country a default value . 
Call your function for three different cities, 
at least one of which is not in the default country .
'''

def describe_city(city,country='Iceland'):
    print('\n'+city+' is in '+country)
    
describe_city('delhi', 'india')
describe_city('reykjavik')
describe_city('lava pools')


