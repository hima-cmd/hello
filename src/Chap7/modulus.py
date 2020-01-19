'''
input() function takes one argument: the prompt, or instructions, 
that we want to display to the user so they know what to do.
'''
# modulo operator (%), 
# which divides one number by another number and returns the remainder:
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")