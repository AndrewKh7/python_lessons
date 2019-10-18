# # task 1
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(c,d+1):
#     print('\t',i,end = "")
# print()
# for i in range(a,b+1):
#     for j in  (tuple((1,))+tuple(range(c,d+1))):
#         print(i*j,'',sep = "\t",end ='')
#     print()

# task 2
# a,b = (int(i) for i in input().split())
a,b = int(input()),int(input())
if a%3:
    if (a+1)%3:
        a += 2
    else:
        a += 1
s = 0
for i in range(a,b+1,3):
    s += i
print (s/(1+(b-a)//3))

