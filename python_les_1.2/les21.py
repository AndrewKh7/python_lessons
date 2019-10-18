# task 1
# s = 0 
# while ...:
#     a=int(input())
#     if not a:
#         break
#     s+=a
# print(s)

# task2
a = int(input())
b = int(input())
a1,b1 = a,b
while a1 and b1:
    if a1>b1:    
        a1 %= b1
    else: 
        b1 %= a1

if a1:
    print(a*b//a1)
else :
    print(a*b//b1) 
