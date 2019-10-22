# task 1
# def closest_mod_5( x ):
#     if x % 5:
#         return (x//5)*5 +5
#     else :
#         return x

# print(closest_mod_5(13))
# print(closest_mod_5(15))
# print(closest_mod_5(16))

# task 2
# def f(num):
#     m = 1
#     for i in range(1,num+1):
#         m *= i 
#     return m

# #
# n,k = map(int, input().split())
# print( f(n) // (f(k) * f(n-k)) )
