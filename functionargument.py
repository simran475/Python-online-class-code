"""function is a block of code which is used to perform a specific task"""
#  def demo():
#     print("hello world")
#     print("i am lucky")

# demo()

# def study (subject,teacher,time):
#     print(f" {subject} is taught by {teacher} at {time}.")

# study("python","mr.ram","10 am")


# def greet(name, greeting="Hello", punctuation="!"):
#     print(f"{greeting}, {name}{punctuation}")

# greet("Alice")

'''1. Positional arguments — matched by order'''
# greet("Alice", "Hi", "!!")
# # ###name="Alice", greeting="Hi", punctuation="!!"

''' 2. Keyword arguments — matched by name, order doesn't matter'''
# greet(greeting="Hey", name="Bob")
###name="Bob", greeting="Hey"#(punctuation uses default)

'''3. Default arguments — fallback used if not provided'''
# greet("Charlie")
# # name="Charlie", greeting="Hello" (default), punctuation="!" (default)

''' You can also mix positional and keyword —
# # but positional args must come first'''
# greet("Dana", punctuation="?")
# # name="Dana" (positional), punctuation="?" (keyword), greeting (defaults)



# def greet(title, name, class_name="python" ): #parameter 
#     print("---------------------------")
#     print (f"{title},{name}")
#     print (f"welcome to class {class_name}")
#     print("---------------------------")

'''positional argument'''
# greet("hi","ram","9")
# greet ("hello","sita","10")

'''keyword argument'''
# greet(title="simran",name="hari",class_name=11)
# greet ("goodmorning",name="simu",class_name=12)
# greet("hi","shyam") # class name is not given use default argument


# def Add(*nums): #  (*args)   # * means all   #only positional argument
#     #print(nums)
#     total =0
#     for n in nums:
#        total+=n
#     print(total)

# Add(2,5,8,3,4,5,6,)
# Add (2,3,4)

# def profile(name,grade,position,marks):
#     print("**************")
#     print(f"""name:{name},
#     grade:{grade}
#     position:{position}
#     marks:{marks}""")
#     print("**************")

# profile(name="Ram",grade="10",position="1st",marks=[47,80,90])






'''when function is same but keyword is different'''

def profile(**data):  ##  **kwargs ->all keyword arguments
    print("************************************************************")
    # print(data)
    for key,values in data.items():
        print(f"{key}:{values}")
    print("************************************************************")
 
profile(name="Ram",grade="10",position="1st",marks=[47,80,90])
profile(name="hari",salary="25000",occupation="teacher")     #here we have different keyword  


# def mix_parameter(name,*args,**kwargs):
#     print(name)
#     print(args)
#     print(kwargs)

# mix_parameter("ram",123,"simu",True,456,89,age=9,num=1) #at first we should write position argument we canot write it later
# # Once you write age=9, you can’t go back to normal values so keyword argument is written in last. 