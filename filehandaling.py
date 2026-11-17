'''Mode	Meaning
'r'	Read (default). Error if the file doesn’t exist
'w'	Write. Erases existing content, creates the file if needed
'a'	Append. Adds to the end, keeps existing content
'x'	Create only. Error if the file already exists'''
# file = open("demo.txt",'a')
# name = input("enter your name: ")
# file.write(f"{name}\n")
# file.close()
# with open("demo.txt", 'a') as file:
#     name = input("enter your name:\n")
#     file.write(name)


with open ("demo.txt",'r')as file:
    # data = file.read()
    # data = file.readline()
    data = file.readlines()
    print(data)
for i, name in enumerate(data):
    name = name[:-1]
    print(f"{i+1}.{name}")

   