'''Higher-Order Functions (HOF)
A higher-order function is a function that takes another function as input OR
returns a function as Output.
Simple Analogy:
A pizza delivery service (HOF) takes your order (function) and delivers pizza (result). The
service doesn't make pizza — it just handles the delivery!'''
# def apply_operation(func, x):
#    return func (x) # Runs whatever function is passed
# def double(n):
#    return n * 2
# def square(n):
#     return n**2
# print(apply_operation(double,5)) #takes another function as input
# print(apply_operation(square,5))
# print(square(5)) #same as hof do
# print(double(5))#do same as hof do


"""map"""
# nums=[12,3,5,34,78,9,77]
# double_num=[]
# for n in nums:
#    double_num.append(2*n)
# print(nums)
# print(double_num)
"""doubling number using map"""
# def double(n):
#    return n * 2
# nums =[12,3,5,34,78,9,77]
# double_num=list(map(double,nums))
# print(double_num)

"""maps with lamda function"""
# nums =[12,3,5,34,78,9,77]
# double_num=list(map(lambda num:num*2,nums))
# print(double_num)

"""string method"""
# name="SIMRAN is lucky"
# print(name.lower())
# print(name.capitalize())
# print(name.title())
# print(name.swapcase())
# name=["simu","ram","shayam"]
# new_name=[]
# for n in name:
#     new_name.append(n.upper())

"""using map with lambda function"""
# print(new_name)
# new_names = list(map(lambda n:n.upper(),name))
# print(new_names)


"""filter"""
# num =[12,3,4,5,678]
# odd_num = list(filter(lambda n: n%2 != 0,num))
# print(odd_num)

# name =["simran","shyam","ram"]
# name_with_s= list(filter(lambda n:n[0] =="s",name))
# print(name_with_s)


"""sorted"""
# num =[12,3,4,6,7,812,35,25,7,6,4,332,1,23]
# sorted_num =sorted(num,reverse=True)
# print(sorted_num)


# name =["simu","ramu","taamu","ravan","sita","laxman"]
# sorted_name =sorted(name,key=len, reverse=True) # reverse sort names from longest to shortest.
# print(sorted_name)


# student =[("simran",1),("simu",9),("ram",91)]
# sorted_s = sorted(student,key=lambda s:s[1])
# print(sorted_s)

"""recursion"""
# def countdown(n):
#     if n==0:
#         return n+1
#     print (n)
#     countdown(n-1)
# countdown(5)


def factorial(n):
    # BASE CASE: factorial of 1 is 1
    if n == 1:
        return 1

    # RECURSIVE CASE: n × factorial of (n-1)
    return n * factorial(n - 1)


print(factorial(5))