# num1 = int( input("please, input num1: ") )
# num2 = int( input("please, input num2: ") )

# print("------------------\n",type(num1),type(num2))

# if num1 > num2:
#     print("num1 > num2")
# else:
#     print("num2 > num1")
        

# state_msg

state_msg = True

str1 = state_msg and "YES" or "NOT"
print(str1)
state_msg = False
str1 = state_msg and "YES" or "NOT"
print(str1)

str1 = "ready" if state_msg else "not ready"
print(str1)


# None is flase
# '' is false

# always is str
var = input('Please, input something: ') # always is str

print(type(var))
if type(var) == int:
    print('it\'s integer number')
elif type(var) == float:
    print('it\'s float number')
elif type(var) == str:
    print('It\'s string')
else:
    print ('It\'s sombody else')

