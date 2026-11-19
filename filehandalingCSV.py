
"""comma seperated value(CSV)
CSV stands for Comma-Separated Values. It's a simple file format that stores data in rows and
columns — like a basic spreadsheet. Each row is a record, and the values in each row are
separated by commas.
A CSV file looks Like this:
Rolt No, Name, Course, Marks
1M, Ram Bahadur,Computer Science, 85"""

# import csv
# Menu="""
# 1.Add data
# 2.exit"""
# with open("student.csv","w",newline =" ")as f:
#     writer= csv.writer(f)
#     # writer.writerow(["Ram",10,12])
#     while True:
#         print(Menu)
#         user_choice=input("Enter your choice:")
#         if user_choice =="1":
#             name =input("enter student name:")
#             grade =input("enter grade:")
#             age = input ("enter age:")
#             writer.writerow([name,grade,age])
#         else:
#             break


import csv
import os
Menu="""
1.Add data
2.exit"""

with open("student.csv","a",  newline ="")as f:
    size =os.path.getsize("student.csv")
    if size ==0:
        writer.writerow([name,grade,age])
    writer= csv.writer(f)
    # writer.writerow(["Ram",10,12])
    while True:
        print(Menu)
        user_choice=input("Enter your choice:")
        if user_choice =="1":
            name =input("enter student name:")
            grade =input("enter grade:")
            age = input ("enter age:")
            writer.writerow([name,grade,age])
        else:
            break


        

