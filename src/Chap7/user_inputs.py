#more examples on user inputs
'''
message = " \n Hello !!! \n"
message += "What kind of rental car would you like : "

user_choice = raw_input(message)
# user_choice = input(message)
print("\nLet me see , if I can find a "+ user_choice +".")

question = "\n Hello \n!! How many people are there in your group ? "
ans = int(input(question))
if ans >= 8:
    print("\n Sorry, Have to wait for table.")
else:
    print("\n Table is ready for you.")
'''

message = "\nHello ! enter a number : "
ans = int(input(message))
if ans % 10 ==0:
    print("\nThe number " + str(ans) + " is multiple of 10.")
else:
    print("\nThe number " + str(ans) + " is not multiple of 10.")