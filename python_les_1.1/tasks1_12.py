#task2
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a+b+c)/2
# print((p*(p-a)*(p-b)*(p-c))**0.5)

# task 2
# val = int(input())
# print( -15 <val <=12 or 14<val<17 or val>=19)

# # task 3
# x = float(input())
# y = float(input())
# op = input()
# if '+' == op:
#     print(x+y)
# elif '-'== op:
#     print(x-y)
# elif '/'== op:
#     if y == 0:
#         print("Деление на 0!")
#     else:
#         print(x/y)
# elif '*'== op:
#     print(x*y)
# elif 'mod' == op:
#     if y == 0:
#         print("Деление на 0!")
#     else:
#         print(x%y)
# elif 'pow' == op:
#     print(x**y)
# elif 'div'== op:
#     if y == 0:
#         print("Деление на 0!")
#     else:
#         print(x//y)

#task 4
# form = input()
# if form == 'треугольник':
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     p = (a+b+c)/2
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# elif form == 'прямоугольник':
#     a = int(input())
#     b = int(input())
#     print(a*b)
# elif form ==  'круг':
#     r = int(input())
#     print(3.14*(r**2))

# task 5
# arr  = sorted([int(input()),int(input()),int(input())])
# print(arr[2],arr[0],arr[1], sep = '\n')

# task 6
# n = int(input())
# if  10<n%100<15:
#     print(n, 'программистов')
# elif n%10==1 :
#     print(n, 'программист')
# elif 1<n%10<5:
#     print(n, 'программиста')   
# else:
#     print(n, 'программистов')

#task
num = int(input())

right = num%10 + num//10%10+num//100%10
left = num//1000%10+num//10000%10+num//100000%10

if left == right:
    print('Счастливый')
else:
    print('Обычный')