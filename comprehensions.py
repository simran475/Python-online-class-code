"comprehension"
"list comprehension" "easy way  to create a list,tuple,set,dictionary"



"""Type	Only if	if/else
List	[x for x in data if cond]	[a if cond else b for x in data]
Set	{x for x in data if cond}	{a if cond else b for x in data}
Dict	{k: v for k, v in data if cond}	{k: (a if cond else b) for k, v in data}
"""  


"without list comprehension"
# even =[]
# for i in range(1,100):
#     if i%2==0:
#         even.append(i)
# print(even)


"with list comprehension"
"syntax for if condition"
"[expression for item in iterable if condition]"
"""nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
# [2, 4, 6] """

# even =[i for i in range(1,101)if i%2==0]
# print(even)

# "syntax for if else condition"
# "[expression  if condition else expression for item in iterable]"
# nums = [1, 2, 3, 4, 5, 6]
# odd_even =["evens"if  n % 2 == 0 else "odd" for n in nums]
# print(odd_even)

"""without comprehension set
"""
# name ="simran"
# vowels = ["a","e","i","o","u"]
# v_letter =set()
# for v in vowels:
#     if v in name:
#         v_letter.add(v)
# print(v_letter)      

# dict = {key: expression for item in iterable}
# dict = {key: expression for item in iterable if conditional}
# dict = {key: expression if conditional else expression for item in iterable}

# days = {
#     "Sunday": "आइतबार",
#     "Monday": "सोमबार",
#     "Tuesday": "मंगलबार",
#     "Wednesday": "बुथबार",
#     "Thursday": "बिहिबार",
#     "Friday": "शुक्रबार",
#     "Saturday": "शनिबार",
# }

# print(days["Sunday"])
# reverse_days = {v: k for k, v in days.items()}
# print(reverse_days)


# words = ["apple", "banana", "apple", "mango", "fig"]
# word_count = {w: (words.count(w) if len(w) > 4 else "small word") for w in words}
# print(word_count)
# {'apple': 2, 'banana': 1, 'mango': 1, 'fig': 'small word'}

# def decorator(func):
#     def wrapper():
#         print("Ribbon")
#         print("Wrapper")
#         func()
#         print("Wrapper")
#     return wrapper


# @decorator
# def cup():
#     print("Cup")

# @decorator
# def jhumka():
#     print("Jhumka")


# cup()
# jhumka()

# login =True 
# def is_login(func):
#     def wrapper():
#         if login:
#             func()
#         else:
#             print("user not login")
#     return wrapper
# @is_login       
# def dashboard():
#     print("welcome back,simran.")

# dashboard()

"""iterator"""
name = "simran"
# for s in name:
#     print(s)


# n =iter(name)
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))

def nums():
    for i in range(1,1000):
        yield i
#     yield 1
#     yield 2
#     yield 3
# n = nums()
# print(next(n))
# print(next(n))
# print(next(n)) 

for num in nums():
   print(num)