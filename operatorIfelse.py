# a=4
# b=8
# #arithmetic operator +, -, *, /, **, %, //
# print(a+b)# output: 12
# print(a-b)# output: -4
# print(a*b)# output: 32
# print(a/b)# output: 0.5
# print(b**a)# output: 4096
# print(a%b)# output: 4
# print(a//b)# output: 0
# print(a//a)
# print(a^b)
# #relational operator >, <, ==, !=, <=, >=
# print(a>b)# output: False
# print(a<b)# output: True
# print(a==b)# output: False
# print(a!=b)# output: True
# print(a<=b)# output: True
# print(a>=b)# output: False  
# print(a is b) #output:false
# print (a is not b)#output ;false


# # Assignment operator +=, -=, *=, /=, **=, //=, %=
# wallet = 1000
# wallet = wallet + 500 # also we can write
# wallet += 500 # wallet = wallet + 500
# print(wallet)# output: 1500

# logical operator and, or, not
# a=True
# b=False
# print(a and b) # output: False # and operator-> if both are true then only output is true
# print(a or b) # output: True #or operator-> if any one is true then output is true
# print(not a) # output: False #not operator-> if a is true then output is false and vice versa
# print(not b) # output: True

# example1
# a = 10
# b = 20
# c = 30
# print(a<b and b<c) # output: True
# print(a>b or b<c) # output: True
# print(not a<b) # output: False

# #example2
# marks = 75
# print(marks>=80 and marks<=100) # output: False
# print(marks>=80 or marks<60) # output: True
# print(not marks>=80) # output: True


# #####conditional flow statements
#   conditional statements # used to perform different actions based on different conditions. In Python, we have the following conditional statements:
#   1. if statement
#   2. if...else statement
#   3. if...elif...else statement

# Example of if...else statement
# is_student = False
# if is_student:
#     print("You are a student.") #output will not be displayed because the value of is_student is False  
# else:
#     print("You are not a student.")#output will be displayed because the value of is_student is False


# #Example of if...else statement
# age = int(input("enter your age:"))
# if age >= 18:
#     print("You are eligible to vote.") #output will be displayed because the value of age is 18 which is greater than or equal to 18
# else:
#     print("You are not eligible to vote.") #output will be displayed because the value of age is 18 which is not greater than or equal to 18


###ANOTHER EXAMPLE
# birds_number=int(input("Enter the number of birds:"))
# if birds_number>1000:
#     print("no need to conserve birds")
# else:
#     print ("conserve birds")



# #   example of if...elif...else statement
# Marks  =int (input("enter your marks:"))
# if Marks >90 and Marks <=100:
#     print("you got A+ grade.")
# elif Marks >= 80 and Marks <=90: #it displays output this time instead of displaying true because if is not in print statement
#     print("You got A grade.") 
# elif Marks >= 70 and Marks <=80:
#     print("You got B+ grade.") 
# elif Marks>=60 and Marks<=70:
#     print("you got Bgrade.")
# elif Marks >= 50 and Marks <=60:
#     print("You got C+ grade.")
# elif Marks >=40 and Marks<=50:
#     print("you got c grade.")
# elif Marks >= 30 and Marks <= 40:
#     print("You got D grade.") 
# else:
#     print("Invalid marks.") 





# ################calculator program
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = input("Enter an operator (+, -, *, /, **, %, //): ")
# if operator == "+":
#     print(f"Add: {num1 + num2}")
# elif operator == "-":
#     print(f"Subtract: {num1 - num2}")
# elif operator == "*":
#     print(f"Multiply: {num1 * num2}")
# elif operator == "/":
#     print(f"Divide: {num1 / num2}")
# elif operator == "**":
#     print(f"Power: {num1 ** num2}")
# elif operator == "%":
#     print(f"Modulus: {num1 % num2}")
# elif operator == "//":
#     print(f"Floor Division: {num1 // num2}")


#### GUI CALCULATOR

# import tkinter as tk

# # ---------- Window ----------
# root = tk.Tk()
# root.title("Calculator")
# root.geometry("340x480")
# root.resizable(False, False)
# root.configure(bg="#1e1e2e")

# expression = ""              # what the user has typed so far
# display_text = tk.StringVar()


# # ---------- Functions ----------
# def press(value):
#     """Add a number or operator to the expression."""
#     global expression
#     expression += str(value)
#     display_text.set(expression)


# def clear():
#     """Clear everything."""
#     global expression
#     expression = ""
#     display_text.set("")


# def backspace():
#     """Delete the last character."""
#     global expression
#     expression = expression[:-1]
#     display_text.set(expression)


# def calculate(event=None):
#     """Work out the answer."""
#     global expression
#     if expression == "":
#         return

#     # Only allow safe characters (numbers and operators)
#     allowed = "0123456789+-*/%. "
#     if any(ch not in allowed for ch in expression):
#         display_text.set("Error")
#         expression = ""
#         return

#     try:
#         result = eval(expression)      # Python does the maths
#         if isinstance(result, float) and result.is_integer():
#             result = int(result)       # show 5 instead of 5.0
#         expression = str(result)
#         display_text.set(expression)
#     except ZeroDivisionError:
#         display_text.set("Cannot divide by 0")
#         expression = ""
#     except Exception:
#         display_text.set("Error")
#         expression = ""


# # ---------- Display ----------
# entry = tk.Entry(
#     root,
#     textvariable=display_text,
#     font=("Arial", 28),
#     justify="right",
#     bd=0,
#     bg="#313244",
#     fg="white",
#     state="readonly",
#     readonlybackground="#313244",
# )
# entry.pack(fill="x", padx=15, pady=20, ipady=15)

# # ---------- Buttons ----------
# frame = tk.Frame(root, bg="#1e1e2e")
# frame.pack(padx=10, pady=5)

# buttons = [
#     ["C", "⌫", "%", "/"],
#     ["7", "8", "9", "*"],
#     ["4", "5", "6", "-"],
#     ["1", "2", "3", "+"],
#     ["0", ".", "//", "**"],
# ]


# def on_click(label):
#     if label == "C":
#         clear()
#     elif label == "⌫":
#         backspace()
#     else:
#         press(label)


# for r, row in enumerate(buttons):
#     for c, label in enumerate(row):
#         if label in ("C", "⌫"):
#             color = "#fddde6"       # red
#         elif label in ("%", "/", "*", "-", "+", "//", "**"):
#             color = "#fab387"       # orange
#         else:
#             color = "#585b70"       # grey
#         tk.Button(
#             frame,
#             text=label,
#             font=("Arial", 18),
#             width=4,
#             height=2,
#             bg=color,
#             fg="white",
#             bd=0,
#             command=lambda l=label: on_click(l),
#         ).grid(row=r, column=c, padx=4, pady=4)

# # Equals button (full width)
# tk.Button(
#     frame,
#     text="=",
#     font=("Arial", 18),
#     height=2,
#     bg="#a6e3a1",
#     fg="black",
#     bd=0,
#     command=calculate,
# ).grid(row=len(buttons), column=0, columnspan=4, sticky="we", padx=4, pady=4)

# # ---------- Keyboard input ----------
# def on_key(event):
#     """Handle keys typed on the keyboard."""
#     key = event.char

#     if key in "0123456789.+-*/%" and key != "":
#         press(key)                      # type // or ** by pressing twice
#     elif event.keysym in ("Return", "KP_Enter") or key == "=":
#         calculate()
#     elif event.keysym == "BackSpace":
#         backspace()
#     elif event.keysym in ("Escape", "Delete") or key.lower() == "c":
#         clear()


# root.bind("<Key>", on_key)

# root.mainloop()


#######   BMI CALCULATOR
# weight = float(input("Enter weight in kg : "))
# height = float(input("Enter height in metres: "))
# bmi = weight / (height ** 2)
# print(f"Your BMI is {bmi:.2f}")
# if bmi < 18.5:
#  print("Category: Underweight")
# elif bmi < 25:
#  print("Category: Normal weight")
# elif bmi < 30:
#  print("Category: Overweight")
# else:
#  print("Category: Obese")


