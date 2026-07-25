# name="simran"
# for l in name:
#     print (l)

###tuple (exactly list but immutable)
student=("ram","shyam","hari")
print (student[0])
for students in student:
    print (students)

# we can not append /change data because it is immutable
##print (student.append("sita")) #wrong in tuple


 #tuple method
#.count() and .index()
student.count(1)
print (students)


print (student.count("shyam"))
print (student.index("ram"))