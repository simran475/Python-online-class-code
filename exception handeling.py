# num1 = float (input("Enter a number:"))
# num2 = float (input("Enter a number:"))
# print (num1 +num2)


"syntax"
"""try:
code
except:
    code"""

"or"
"""try:
    # code that might cause an error

except ErrorType:
    # runs if that specific error happens

except (ErrorType1, ErrorType2):
    # one block for multiple error types

except ErrorType as e:
    # "as e" stores the error object so you can print it

except Exception as e:
    # catches any other error (keep this last)

else:
    # runs only if NO error happened

finally:
    # always runs"""

# try:
#     num1 = float (input("Enter a number:"))
#     num2 = float (input("Enter a number:"))
#     print (num1 +num2)
# except:
#     print("error!")
# print("program ended sucessfully")




# try:
#     # Code that might fail
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter a number: "))
#     result = num1 / num2  # division can raise ZeroDivisionError

# except ValueError:
#     # Input was not a number (e.g. "abc")
#     print("Please enter numbers only!")

# except ZeroDivisionError:
#     # Second number was 0
#     print("You cannot divide by zero!")

# except EOFError:
#     # Input ended unexpectedly (e.g. Ctrl+D)
#     print("No input received!")

# except KeyboardInterrupt:
#     # User pressed Ctrl+C
#     print("Program cancelled by user.")

# except Exception as e:
#     # Any other error (keep this one last)
#     print("Unexpected error:", e)

# else:
#     # Runs only if there was no error
#     print("Result:", result)

# finally:
#     # Always runs
#     print("program ended")

# try:
#     num1 = float(input("Enter a number: "))
#     num2 = float(input("Enter a number: "))

#     if num1 < 0 or num2 < 0:
#         # raise our own error; Python jumps to the except block
#         # raise ValueError("Negative numbers are not allowed")
#         raise Exception("negative number canot be added ")
# except Exception as e:
#     print(e)  # prints the message from raise (or Python's own message)

# else:
#     print(num1 + num2)

# finally:
#     print("program ended")

import csv
import os

MENU = """
===== Student Records =====
1. Add student
2. View students
(any other key to exit)
"""

while True:
    print(MENU)
    user_choice = input("Enter your choice (1/2): ")

    if user_choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        score = input("Enter student score: ")

        try:
            # "a" mode appends and creates the file if it does not exist
            with open("students.csv", "a", newline="") as file:
                writer = csv.writer(file)
                file_size = os.path.getsize("students.csv")
                if file_size == 0:  # empty file, so write the header once
                    writer.writerow(["Name", "Grade", "Score"])
                writer.writerow([name, grade, score])
            print("Student added successfully.")
        except PermissionError:
            print("You do not have permission to edit this file. "
                  "It may be open in another program.")

    elif user_choice == "2":
        try:
            with open("students.csv", "r", newline="") as file:
                reader = list(csv.reader(file))

            if reader and reader[0] == ["Name", "Grade", "Score"]:
                reader = reader[1:]  # slicing: skip the header row (only if it exists)
            reader = [row for row in reader if len(row) >= 3]  # skip blank/broken rows

            if not reader:
                print("No student records found in:", os.path.abspath("students.csv"))

            for line in reader:
                print("************")
                print("Name:", line[0])
                print("Grade:", line[1])
                print("Score:", line[2])
                print("************")
        except FileNotFoundError:
            print("This file does not exist.")
        except PermissionError:
            print("Cannot read the file. It may be open in another program (e.g. Excel).")

    else:
        print("Program ended.")
        break