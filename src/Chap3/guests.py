# Using List methods : insert() , append()

guest_list = ['Rajit','Abhi','Anvi']
print(" List : ")
print(guest_list)

print("Hello ! " + guest_list[0] +" , You are invited to my party .")
print("Hello ! " + guest_list[1] +" , You are invited to my party .")
print("Hello ! " + guest_list[2] +" , You are invited to my party .\n")

print("Guest : " + guest_list[0] + ", can't make it to the party.\n")
guest_list[0]='Neha'

print("Hello ! " + guest_list[0] +" , You are invited to my party .")
print("Hello ! " + guest_list[1] +" , You are invited to my party .")
print("Hello ! " + guest_list[2] +" , You are invited to my party .\n")

print("Hello Everyone ! Found a bigger table for the party, so more guests.\n")

guest_list.insert(0, 'Ammamma')
guest_list.insert(2, 'Thatha')
guest_list.append('Akul')
print("New guest list : ")
print(guest_list)

print("Hello ! " + guest_list[0] +" , You are invited to my party .")
print("Hello ! " + guest_list[1] +" , You are invited to my party .")
print("Hello ! " + guest_list[2] +" , You are invited to my party .")
print("Hello ! " + guest_list[-3] +" , You are invited to my party .")
print("Hello ! " + guest_list[-2] +" , You are invited to my party .")
print("Hello ! " + guest_list[-1] +" , You are invited to my party .\n")



