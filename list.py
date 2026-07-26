# ##Data structures
# ##Lists
# name=["simran","ram","shyam"]
# # positive indexing [0,1,2] and negative indexing [-3,-2,-1]
# # print(name)
# # print(name[0]) #output: simran
# # print(name[1]) #output: ram
# # print(name[2]) #output: shyam
# # print(name[-3]) #output: simran
# # print(name[-2]) #output: ram
# # print(name[-1]) #output: shyam
# # print(name[0:2]) #output: ['simran', 'ram'] #slicing  #end is not included
# # print(name[1:3]) #output: ['ram', 'shyam'] #slicing
# # print(name[0:3]) #output: ['simran', 'ram', 'shyam'] #slicing #we have to give extra index to include the last element
# # print(name[0:]) #output: ['simran', 'ram', 'shyam'] #slicing #if we don't give the end index then it will take all the elements from the start index to the end of the list
# # print(name[:3]) #output: ['simran', 'ram', 'shyam'] #slicing #if we don't give the start index then it will take all the elements from the start of the list to the end index
# # print(name[:]) #output: ['simran', 'ram', 'shyam'] #slicing #if we don't give the start and end index then it will take all the elements from the list
# # print(name[::2]) #output: ['simran', 'shyam'] #slicing #if we give the step index then it will take all the elements from the start index to the end index with the given step index
# # print(name[::-1]) #output: ['shyam', 'ram', 'simran'] #slicing #if we give the step index as -1 then it will take all the elements from the end index to the start index
# # print(name[1:3:2]) #output: ['ram'] #slicing #if we give the step index then it will take all the elements from the start index to the end index with the given step index


   
# #list methods
    
# name.append("sita")
# print(name)
# name.remove("ram")
# print(name)
# print(len(name)) #output: 3 #it will give the length of the list
# name.insert(3,"ram")
# print(name)
# name.pop(2)
# print(name)
# name.sort()
# print(name)
# name.reverse()
# print(name)
# name.clear()
# print(name)
# print(len(name)) #output: 0 #it will give the length of the list
# name1=["simran","ram","shyam"]
# name2=["sita","gita","rita"]
# name3=name1+name2
# print(name3)
# print(name3.index("ram")) #output: 1 #it will give the index of the given element
# print(name3.count("ram")) #output: 1 #it will give the count of the given element



########membership perator ->in, not in # membership operators are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
# student=["simran","ram","shyam"]
# print("simran" in student) #output: True
# print("sita" in student) #output: False
# print("simran" not in student) #output: False
# print("sita" not in student) #output: True


# example of membership operator
# name=(input("Enter your name: "))
# if name in student:
#     print("You are a student.")
# else:
#     print("You are not a student.")


# ###Range
# print(list(range(10))) #output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #it will give the list of numbers from 0 to 9 #10 is the stopping value
# print(list(range(2, 10))) #output: [2, 3, 4, 5, 6, 7, 8, 9] #it will give the list of numbers from 2 to 9 #10 is the stopping value and 2 is the starting value
# print(list(range(2, 10, 2))) #output: [2, 4, 6, 8] #it will give the list of numbers from 2 to 9 with a step of 2 #there will be gap of 2 between the numbers



# ##for loop
# for i in range(2):
#     print("my name is simran") 
#     print ("i am learning python")
# print("i am notlearning python") #this statement is not part of the for loop because it is not indented

# students=["simran","ram","shyam"]
# for s in students: #for loop will iterate through the list of students and print each name one by one
#     print(s) #output: simran ram shyam #it will print the names of the students one by one




# # Assignment1
# # fruits=["apple","banana","grapes","mango","orange"]
# # print(fruits)
# # print(fruits[0:6:4]) #output: ['apple', 'orange'] #it will print the first and last element of the list
   


# mixed=[1,1.5,"simran",True,False]
# print(mixed) #output: [1, 1.5, 'simran', True, False] #it will print the list of mixed data types
# print(type(mixed)) #output: <class 'list'> #it will print the type of the list
# for item in mixed:
#     print(item, "→", type(item))



# # Assignment2
# students=["simran","ram","shyam","gita","rita","mita","sita"]
# name=input("Enter your name: ")
# if name in students:
#     print(" student found")
# else:
#     print("student not found")    


# # membership operator on string
# sentence="my name is simran"
# print("simran" in sentence) #output: True #it will check whether the string "simran" is present in the sentence or not
# print("sita" in sentence) #output: False #it will check whether the string "sita" is present in the sentence or not

# ### membership operator on list
# students=["simran","ram","shyam"]
# name=input("Enter your name: ")
# print(name in students) #output: True or False #it will check whether the name entered by the user is present in the list of students or not
      

############

# print(range(10))
# print(list(range(11)))#output:0to 10 inlist
# print(list(range(1,11))) # output :1to 10
# print(range(1,11))
# print(list(range(10,30,2))) # even number from 10 to 30
# print(list(range(1,20,2))) #odd number from 1 to 20


####multiplication
# print(list(range(5, 51, 5)))


  ######loop
# for s in range (15):
#     print ("python is fun")

# for i in range (10,0,-1):  ##to print number in reverse
#     print(i)

# #to print square
# for i in range(1, 11): 
#     square = i ** 2
#     print( i, "squared =", square)
  

##
numbers =[1,2,3,4,5,6,7,8,9,10]
# print("index "," numbers")
# for i in range(len(numbers)):
#     print(i,"\t",numbers[i])


# for n in numbers:
#     if n%2==0:
#         print (f"{n} is even numer") # using f string
#     else:
#         print (n,"is odd number")


# target = (input("enter a number:"))
# if target in numbers:
#     print(target, "is in the list")
# else:
#     print(target, "is not in the list")