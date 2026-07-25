# a=4
# b=8
# #arithmetic operator +, -, *, /, **, %, //
# print(a+b)# output: 12
# print(a-b)# output: -4
# print(a*b)# output: 32
# print(a/b)# output: 0.5
# print(b**a)# output: 3
# print(a%b)# output: 4
# print(a//b)# output: 0

# #relational operator >, <, ==, !=, <=, >=
# print(a>b)# output: False
# print(a<b)# output: True
# print(a==b)# output: False
# print(a!=b)# output: True
# print(a<=b)# output: True
# print(a>=b)# output: False  


# Assignment operator +=, -=, *=, /=, **=, //=, %=
# wallet = 1000
# #wallet = wallet + 500 # also we can write
# wallet += 500 # wallet = wallet + 500
# print(wallet)# output: 1500

#logical operator and, or, not
# a=True
# b=False
# print(a and b) # output: False # and operator-> if both are true then only output is true
# print(a or b) # output: True #or operator-> if any one is true then output is true
# print(not a) # output: False #not operator-> if a is true then output is false and vice versa
# print(not b) # output: True

#example1
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


######conditional flow statements
  #conditional statements # used to perform different actions based on different conditions. In Python, we have the following conditional statements:
  #1. if statement
  #2. if...else statement
  #3. if...elif...else statement

#Example of if...else statement
# is_student = False
# if is_student:
#     print("You are a student.") #output will not be displayed because the value of is_student is False  
# else:
#     print("You are not a student.")#output will be displayed because the value of is_student is False


# #example of if...else statement
# age = int(input("enter your age:"))
# if age >= 18:
#     print("You are eligible to vote.") #output will be displayed because the value of age is 18 which is greater than or equal to 18
# else:
#     print("You are not eligible to vote.") #output will be displayed because the value of age is 18 which is not greater than or equal to 18
 


# #   example of if...elif...else statement
# Marks  =int (input("enter your marks:"))
# if Marks >= 80 and Marks <= 100: #it displays output this time instead of displaying true because if is not in print statement
#     print("You got A grade.") 
# elif Marks >= 60 and Marks < 80:
#     print("You got B grade.") 
# elif Marks >= 40 and Marks < 60:
#     print("You got C grade.") 
# elif Marks >= 0 and Marks < 40:
#     print("You got D grade.") 
# else:
#     print("Invalid marks.") 





################calculator program
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter an operator (+, -, *, /, **, %, //): ")
if operator == "+":
    print(f"Add: {num1 + num2}")
elif operator == "-":
    print(f"Subtract: {num1 - num2}")
elif operator == "*":
    print(f"Multiply: {num1 * num2}")
elif operator == "/":
    print(f"Divide: {num1 / num2}")
elif operator == "**":
    print(f"Power: {num1 ** num2}")
elif operator == "%":
    print(f"Modulus: {num1 % num2}")
elif operator == "//":
    print(f"Floor Division: {num1 // num2}")