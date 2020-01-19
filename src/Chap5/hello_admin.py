#Hello Admin

user_names = ['abhi','anvi','rajit','hima','admin','abcd','xyz','one','two']

print("Hello !!\n")

for user in user_names:
    
    if user: #check if list is empty
        if user != 'admin' :
            print("Hello "+ user +" , thank you for logging in again.")
        else:
            print("Hello admin, would you like to see a status report?")
    else:
        print("\nWe need to find some users!")
