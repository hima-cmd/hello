# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username .

current_users = ['Abhi','Anvi','Rajit','Hima','Admin','ABCD']
new_users = ['laxmi','rao','ravi','neha','ADMIN','abcd']
'''
# current_users
print(current_users)
temp = []
for c_user in current_users:
    temp.append(c_user.lower())
        
current_users = temp[:] 
print("Current users list in lower :")
print(current_users) 

for user in new_users: 
    user = user.lower() 
    print("checking for : "+user)
    if user in current_users:
        print("Username "+ user +" ,already used. Enter new username.\n")
    else:
        print("Username "+ user +" is available.\n")
'''
flag = False
for user in new_users: 
    user = user.lower() 
    print("checking for : "+user)
    for c_user in current_users:
        if user == c_user.lower():
            print("Username "+ user +" ,already used. Enter new username.\n")
            flag = True
            break
    if flag == False:  
        print("Username "+ user +" is available.\n")
      