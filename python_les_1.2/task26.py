#task 1 
# sum = int(input())
# l = [sum,]
# while sum:
#     l.append(int(input()))
#     sum+=l[-1]
# for i in l:
#     sum += i*i
# print(sum)

# task 2
# n = int(input())
# cnt = 1
# while n:
#     # [ (print(cnt),n -= 1) for j in range(cnt)] 
#     r = cnt if n>cnt else n
#     for i in range(r):
#         print(cnt, end =' ')
#         n -= 1
#     cnt += 1

# task 3
# lst = [int(i) for i in input().split()]
# x = int(input())
# res = []
# cnt = 0
# for i in lst:
#     if i == x: res.append(cnt) 
#     cnt += 1
# if res == []:
#     print('Отсутствует')
# else:
#     [print(i, end = ' ') for i in res]

# task 4
# input_mat = []
# while ...:    
#     str1 = input()
#     if str1 == 'end': break
#     input_mat.append([int(i) for i in str1.split()])
# output_mat = [ [0] * len(input_mat[0]) for i in range(len(input_mat)) ]
# for i in range( len( input_mat ) ):
#     for j in range( len( input_mat[0] ) ):
#         output_mat[i][j] += input_mat[0][j] if i == len( input_mat ) - 1 else input_mat[i+1][j]
#         output_mat[i][j] += input_mat[i][0] if j == len( input_mat[0] ) - 1 else input_mat[i][j+1]
#         output_mat[i][j] += input_mat[i-1][j] + input_mat[i][j-1]
# for i in output_mat:
#     [print(j,end = " ") for j in i]
#     print()
    
# task 4
n = int(input())
mat = [[0]*n for i in range(n)]
cnt = 1
temp = 0 + n
i = 0
j = 0
if n % 2: mat[ n//2 ][ n//2 ] = n*n
while cnt <= n*n-1:
    for j in range(j,temp-1): 
        mat[i][j] = cnt
        cnt += 1
    j+=1
    for i in range(i,temp-1):
        mat[i][j] = cnt
        cnt += 1
    i+=1
    for j in range(j,n-temp,-1): 
        mat[i][j] = cnt
        cnt += 1
    j-=1
    for i in range(i,n-temp,-1):
        mat[i][j] = cnt
        cnt += 1
    j+=1
    temp-=1

for i in mat:
    [print(j,end = ' ') for j in i]
    print()


