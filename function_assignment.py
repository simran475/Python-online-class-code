# ####assignment
# def square(n):
#    return n**2

# print(square(4))
# square(5)



# #assignment 2
# def is_even(n):
#     if n%2==0:
#        return True
#     else:
#         return False
# print(is_even(5))
# print(is_even(2))



# ######assignment 3
# def rectangle_area(l,b):
#     return l*b

# print(rectangle_area(7,4))

# //4
# def greet_user(name):
#     return(f"good morning {name}")

# print (greet_user("simran"))

#///5
# def power(base,exponent=2):
#      return(base**exponent)
# print(power(5,5))  


##//6
# def create_greeting(name,greeting="hello",punctuation="!"):
#     return(f"{name} {greeting}{punctuation}")
# print(create_greeting("simran"))

##//7
# def calculate_tax(amount, tax_rate):
#     return amount * tax_rate / 100

# print(calculate_tax(1000, 13))




# list["sudam","ram",1], tuple, set, dictionary
# array["sudam","ram",1], object


# Assignment 1

# def square(n):
#     return n**2


# print(square(4))
# print(square(7))


# Assignment 2


# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# def is_even(n):
#     if n % 2 == 0:
#         return f"{n} is even number"
#     else:
#         return f"{n} is odd number"


# print(is_even(6))
# print(is_even(9))


# power(4)


# Assignment 2
# def power(base, expo=2):
#     return base**expo

# print(power(10, 3))
# print(power(12))


# Assignment 4
# def mul(*nums):
#     if len(nums) == 0:
#         return 0
#     total = 1
#     for n in nums:
#         total *= n
#     return total


# print(mul(3, 4, 5, 1))

# print(mul())


# def longest_words(*words):
#     lw = None
#     w_count = 0
#     for word in words:
#         if w_count < len(word):
#             w_count = len(word)
#             lw = word
#     return f"Longest word is {lw} with word count {w_count}"


# print(longest_words("hello", "banana", "ram", "hiiiiiiiiiiiii"))


# Assignment 9

# total_calls = 0

# def p():
#     global total_calls
#     total_calls += 1
#     print("function is called")

# def pp():
#     print(total_calls)

# p()
# p()
# p()
# p()
# p()

# pp()


# Assignment 11

# def filter_students(**kwargs):
#     students = [
#         {"name": "Ram", "age": 12, "grade": 10},
#         {"name": "Shyam", "age": 11, "grade": 10},
#         {"name": "Hari", "age": 10, "grade": 9},
#         {"name": "Sita", "age": 9, "grade": 8},
#     ]

#     results = []
#     for student in students:
#         # print(student)
#         match = True
#         for key,value in kwargs.items():
#             # print(student[key])
#             if student.get(key) != value:
#                 match = False

#         if match:
#             results.append(student)

#     print(results)


# filter_students(grade=1)


# def demo():
#     """
#     Please follow these steps
#         1. this is that
#         2. yooooo
#         3.helloo
#     """

#     print("hello")

# print(demo.__doc__)
# help(demo)


# import calc

# print(calc.add(1, 2, 3, 4))
# print(calc.mul(1, 2, 3, 4))
# print(calc.sub(1, 2))

# from calc import *

# print(add(1, 2, 3, 4))
# print(mul(1, 2, 3, 4))
# print(sub(1, 2))


# from calc import add, mul
# print(add(1, 2, 3, 4))
# print(mul(1, 2,3,45))



# from calc import add as a  # Importing with new name
# print(a(1,3,4,5,6))
