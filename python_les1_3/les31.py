# task 1
# def f(x):
#     if x<=-2:
#         f = 1-(x+2)**2
#     elif -2<x<=2:
#         f = -x/2
#     else:
#         f = (x-2)**2+1
#     return f
# print(f(1))

# task 2
def modify_list(l):
    # temp = []
    i = 0
    while i < len(l):
        if l[i] % 2:
            l.pop(i)
        else:
            l[i] = l[i]//2
            i+=1
        

list1 = [1, 2, 3, 4, 5, 6]
print( modify_list(list1) )
print(list1)
print( modify_list(list1) )
print(list1)
