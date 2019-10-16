#task 1
A = int(input())
B = int(input())
H = int(input())

if H <= A:
    print('Недосып')
elif H>=B:
    print('Пересып')
else:
    print('Это нормально')

#task2

year = int(input())

if (year%400 == 0) or (year%4==0 and not year%10==0):
    print('Высокосны')
else:
    print('Обычный')