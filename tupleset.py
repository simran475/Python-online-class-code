'''for loop'''
# name="simran"
# for i in name:
#     print (i)

'''tuple (exactly list but immutable)''' #collection of data which we canot change
student=("ram","shyam","hari")
print(student)
# print (student[0])
# for s in student:
#     print (s)

'''# we can not append /change data because it is immutable'''
# print (student.append("sita")) #wrong in tuple


'''tuple method
.count() and .index()'''
# print (student)
# print (student.count("shyam"))
# print (student.index("ram"))

'''single tuple'''
# demo=("sudan")
# demo=("sudan") # string
# demo=(2,)  # tuple # we need to give comma after a number  if it is single so that it recoganize it is a tuple otherwise it will show int
# print(type(demo))





'''Set   {}-> it is unordered ,  and donot print repeted data'''
# we cannot give indexing i this because it is not in order
# students={"hari","ram","shyam","nita","gita"}
# print (students)

# ram_hobbies={"dancing","eating","singing","reading"}
# sita_hobbies={"painting","cooking","singing","reading"}
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
# superset =ram_hobbies.issuperset(sita_hobbies) #issuperset is used to check if ram is superset of  sita or not
# print(superset)#output :false 
# subset =ram_hobbies.issubset(sita_hobbies)
# print(subset)#output:false
# ram_hobbies.add("swimming")
# print(ram_hobbies)
# ram_hobbies.remove("dancing")
# print(ram_hobbies)
# ram_hobbies.pop()#remove randomdata
# print(ram_hobbies)
# # ram_hobbies.pop(0)#wrong because set is unordered so we cannot give index
# ram_hobbies.clear()#remove all data
# print(ram_hobbies)#it will print empty set #output:set()

