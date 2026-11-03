'''A dictionary is a collection of key-value pairs. Keys must be unique and immutable (strings, numbers, tuples); values can be anything.
use {}'''
'''as we know that both set an dictionary us
to make an empty dictonary we can do this-> data={}
to make an empty set we can do this-> data= set()
'''
# for dictionary we do this
# student ={"name":"simran","Age":18,"grade":"A+"}
# print(student)
# print(student["name"])
# print(student["Age"])
# print (student.get ("id",101))
# student["name"]="simu"# replace the value of name
# print(student)
# print(student.keys())
# print(student.values())

# Student={
#     "name":"simran","Age":18,"grade":"A+","phone number":9805412586
# }

# Student["Age"]=12
# Student["job"]="doctor" # even it is not in dictonary we can add it like this
# Student.update({"name":"ram","grade":"A"})
# Student.pop("grade")
# Student.popitem("phone number")
# Student.copy("name")

# print(Student["grade"])
# # print(Student[0])# this will give error becaude we canot access dictionary by index we can only acess it by key 
# print(Student.get("phone number"))
# print(Student.get("job"))# when we try to print key that donnot exist while using it will print none
# print(Student.get("job","Any"))# and if this key value donot exist and want to exist we put default value
# print(Student.keys()) #it prints all the keys in list
# print(Student.values()) #prints values in list
# print(Student.items()) #print both keys and values in tuple inside list

# for item in Student.items():
#    print(item)
#    key, value =item
#    print(f"{key}:{value}")

# Student["Age"]=19 # this will replace value of age
# print(Student)
# Student["class"]=9 #if this key donot exist it will add
# print(Student)
#   # to add multiple values we need to create another dictionary
#   #example
# Student.update({"roll_no":7,"height":5})
# print(Student)

'''while loop'''
# while True:
#     print("my name is simran and i am very lucky.") #it will go on infinite loop
#     break #it will not let it go in infinite loop

# i=1
# while i<=5:
#     print(i)
#     i+=1 

# count = 1

# while True:                  # the condition is always True, so the loop never stops by itself
#     print(count)
#     if count == 5:           # check if count has reached 5
#         break                # break stops the loop, even though the condition is still True
#     count = count + 1        # add 1 to count and repeat

# print("Loop finished")       # this runs after the loop stops

# for i in "hello":
#     pass # pass is a null statement — it does absolutely nothing.
# # It's used as a placeholder when Python syntax requires a statement (like inside a loop, function, class, or if-block),
# #  but you don't want any code to run there yet


''' here is a simple example of a while loop that counts from 1 to 5 and prints each number. 
The loop continues as long as the condition (i <= 5) is true. Inside the loop, 
we print the current value of i and then increment it by 1. Once i becomes greater than 5, the loop exits. '''

''' while-else '''
# i=1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("False")


'''# #password example'''
# name="simran"
# password="i am lucky"
# attempt=0
# print("*************************************")
# while True:
#     user_name=(input("enter user name:"))
#     user_password=(input("enter password:"))
#     attempt+=1
#     if user_name == name and user_password ==password:
#         print("welcome to dasboard")
#         break
#     if attempt==2:
#         print("you have only 1 chance left")
    
#     print("*************************************")
#     if attempt>2:
#             print("account locked")
#             break



'''continue #continue skips the rest of the current loop iteration 
and jumps straight to the next iteration — it does not exit the loop,
   it just skips what's left in the current cycle.'''
i=0
while True:
    i+=1
    # if i>10:
    #     break
    if i==5:
        continue
    print (i)
    