"comprehension"
"list comprehension" "easy way  to create a list,tuple,set,dictionary"

"without list comprehension"
# even =[]
# for i in range(1,100):
#     if i%2==0:
#         even.append(i)
# print(even)

"with list comprehension"
"syntax"
"[expression for item in iterable if condition]"
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
# [2, 4, 6] 