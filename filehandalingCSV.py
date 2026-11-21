
"""comma seperated value(CSV)
CSV stands for Comma-Separated Values. It's a simple file format that stores data in rows and
columns — like a basic spreadsheet. Each row is a record, and the values in each row are
separated by commas.
A CSV file looks Like this:
Rolt No, Name, Course, Marks
1M, Ram Bahadur,Computer Science, 85"""

import csv
Menu="""
1.Add data
2.exit"""
with open("student.csv","w",newline ="")as f:
    writer= csv.writer(f)
    writer.writerow([f"name,grade,age"])
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




# import csv
# import os

# Menu="""
# 1.Add data
# 2.read
# 3.search
# 4.exit"""
# with open("student.csv", "r+", newline="") as f:
#     writer = csv.writer(f)                 # create writer FIRST
#     size = os.path.getsize("student.csv")
#     if size == 0:                          # file is empty → write header once
#         writer.writerow(["Name", "Grade", "Age"])

#     while True:
#         print(Menu)
#         user_choice = input("Enter your choice:")
#         if user_choice == "1":
#             name = input("enter student name:")
#             grade = input("enter grade:")
#             age = input("enter age:")
#             writer.writerow([name, grade, age])
#         elif user_choice=="2":
#             reader=list(csv.reader(f) ) 
#             print(reader ) 
#         elif user_choice =="3":
#             name=input("enter student name:")
#             for r in reader:
#                 if name in r :
#                     print(r)
#         else:
#             break

# import csv

# # 1. Read all rows into a list
# with open("student.csv", "r", newline="") as f:
#     rows = list(csv.reader(f))

# # 2. Change the data in the list
# for row in rows:
#     if row[0] == "Ram":      # row[0] is the Name column
#         row[1] = "12"        # row[1] is the Grade column

# # 3. Write everything back ("w" replaces the old file content)
# with open("student.csv", "w", newline="") as f:
#     csv.writer(f).writerows(rows)


# data =[["name","grade","age","status"]]
# with open("student.csv", "r", newline="") as f:  
#    reader = list(csv.reader(f))[1:]      # 1. read all rows, skip the header
#    for row in reader:
#      row.append("active")              # 2. add "active" at the end of each row
#      data.append(row)                  #    collect the changed rows in data

# with open("student.csv", "w", newline="") as f:   # 3. write back
#     writer = csv.writer(f)
#     writer.writerows(data)            #    write all rows at once
