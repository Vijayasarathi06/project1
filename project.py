 ##Project1
user_input=str(input("enter the value of user input"))
words=user_input.split()
a=""
for i in  words:
    a+=i[0].upper()
print(a)
