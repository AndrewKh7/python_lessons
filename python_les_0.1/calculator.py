x = float (input('First number: '))
y = float (input('Second number: '))
operating = input ('Operating ')

result = None

if operating == '+':
    result = x + y
elif operating == '-':
    result  = x - y
elif operating == '*':
    result = x*y
elif operating == '/':
    result = x/y
else:
    print('None')

if result is not None:
    print("result: ", result)
