'''
'Reading the contents of file as whole.'
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

filename = 'pi_digits.txt'
'Reading line by line in the text file'
'''
with open(filename) as file_object: 
    for line in file_object:
        print(line.rstrip())
'''
'Reading line by line from text file and storing in a list'

with open(filename) as file_object:
    lines = file_object.readlines() 

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ") 
if birthday in pi_string:
       print("Your birthday appears in the first million digits of pi!")
else:
       print("Your birthday does not appear in the first million digits of pi.")

print(pi_string)
print(len(pi_string))