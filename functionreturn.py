def mul(*nums):
    total = 1
    for n in nums:
        total *= n
    return total

print(mul(3, 2))  # 6

# def test():
#     print("Second")
#     return          #returns back and go back to the caller so that code downwards it donot run
#     print("First")
#     return
#     print("Second")
#     return

# test()

# yoo="hello"
'''###local variable'''
# def demo():
    
#     yoo="sudam" #local varible #we can use it where we define it
#     print(yoo)
# demo()
# print(yoo)##can not print outside that function



'''#global varible'''
# name="ram"
# def demo():
#     print("age:15")
# demo()
# print (name)
 
'''#  #making local varible a global varible'''
# def demo():
#     global yoo # we can make a local varible a globle varible by this method
#     yoo="sudam" #local varible #we can use it where we define it
#     print(yoo)
# demo()
# print(yoo)##can not print outside that function

# # example:
# x = 100      # Global variable

# def test():
#     x = 50   # Local variable
#     print("Inside function:", x)

# test()
# print("Outside function:", x)
# # The local variable x exists only inside the function and does not affect the global x.  

'''number geuss game'''
from random import randint
player ={"ram":4,"shyam":5}
while True:
    user_choice= input("do you want to play game(y/n?)")
    if user_choice == "y":
        player_name = input("enter player name:")
        Random_num = randint(1,100)
        attempt=0
        while True:
            num =int(input("enter a number:"))
            attempt+=1
            if num == Random_num:
                print("you have gussed it right")
                if not player.get(player_name) or player.get(player_name)>attempt:
                   player[player_name]= attempt
                break
            elif num<Random_num:
                print("too low")
            elif num>Random_num:
                print("too high")
            else:
                print("invalid input")
    elif user_choice == "n":    
        break
    else :
        print("invalid user input")       
        

    