'''Mode	Meaning
'r'	Read (default). Error if the file doesn’t exist
'w'	Write. Erases existing content, creates the file if needed
'a'	Append. Adds to the end, keeps existing content
'x'	Create only. Error if the file already exists'''
# file = open("demo.txt",'a')
# name = input("enter your name: ")
# file.write(f"{name}\n")
# file.close()
# with open("demo.txt", 'a') as file:
#     name = input("enter your name:")
#     file.write(f"{name}\n")


# with open ("demo.txt",'r')as file:
#     # data = file.read()
#     # data = file.readline()
#     data = file.readlines()
#     print(data)
# for i, name in enumerate(data):
#     name = name[:-1]
#     print(f"{i+1}.{name}")


# MENU = """
# 1.Get Student Data
# 2.Add Student
# 3.Exit
# """

# while True:
#     print(MENU)
#     user_choice = input("Enter your choice: ")
#     if user_choice == "1":
#         file = open("students.txt", "r")
#         students = file.read()
#         students = students.split(", ")[:-1]
#         for i, s in enumerate(students):
#             print(f"{i+1}:{s}")
#     elif user_choice == "2":
#         name = input("Enter Student Name: ")
#         file = open("students.txt", "a")
#         file.write(f"{name}, ")
#         file.close()
#     elif user_choice == "3":
#         break
#     else: 
#         print("Invalid user input..")

# from datetime import date
# name =input("enter name of present student(comma seperated)")
# # print(name)
# file =open("attendance.txt","a")
# file.write(f"Date:{date.today()}|Present:{name}\n")
# file.close()

file =open("attendance.txt","r")
# data =file.readline()
# data =file.readlines()
data =file.read()
print(data)
file.close()