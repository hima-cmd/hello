#seeing the world

visit_list = ['italy','swiss','usa','new zealand','thailand']
print(visit_list)

#using sorted() to sort the list 
# without modifying the list.
print("using sorted() on visit_list.")
print(sorted(visit_list))
print("Visit List : ")
print(visit_list)
print("using sorted(reverse=True) on visit_list.")
print(sorted(visit_list,reverse=True))
print("Visit List : ")
print(visit_list)

#changing order of the list permanently
visit_list.reverse()
print("Changed order List : ")
print(visit_list)

visit_list.reverse()
print("Back to previous List : ")
print(visit_list)

visit_list.sort()
print("Sort list : ")
print(visit_list)

visit_list.sort(reverse=True)
print("Reverse Sort list : ")
print(visit_list)

print("Length of the visit list : "+str(len(visit_list)))




