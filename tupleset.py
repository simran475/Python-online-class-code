# name="simran"
# for l in name:
#     print (l)

###tuple (exactly list but immutable)
# student=("ram","shyam","hari")
# print (student[0])
# for students in student:
#     print (students)

# we can not append /change data because it is immutable
##print (student.append("sita")) #wrong in tuple


 #tuple method
#.count() and .index()
# student.count(1)
# print (students)


# print (student.count("shyam"))
# print (student.index("ram"))


# # demo=("sudan")
# demo=("sudan") # string
# demo=(2,)  # tuple # we need to give comma after a number  if it is single so that it recoganize it is a tuple otherwise it will show int
# print(type(demo))






##### Set   {}-> it is unordered ,  and donot print repeted data
# we cannot give indexing i this because it is not in order
# students={"hari","ram","shyam","nita","gita"}
# print (students)

ram_hobbies={"dancing","eating","singing","reading"}
sita_hobbies={"painting","cooking","singing","reading"}
# print(ram_hobbies)
# print(sita_hobbies)
# union =ram_hobbies.union(sita_hobbies) #.union is used for the union of two set
# print(union)

# intersection=ram_hobbies.intersection(sita_hobbies) # intersection is used for intersection
# print(intersection)

# difference=ram_hobbies.difference(sita_hobbies) #difference # ram is in before this will show what is difference in ram
# print(difference)
# difference=sita_hobbies.difference(ram_hobbies) #difference # sita is in before this will show what is difference in sita
# print(difference)