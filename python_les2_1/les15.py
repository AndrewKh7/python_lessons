################################################# task 1 'MoneyBox'
# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.val = 0

#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         return  False if self.val+v > self.capacity else True
#     def add(self, v):

#         # положить v монет в копилку
#         self.val = self.val + v if self.val < self.capacity else self.val

################################################# task 2

class Buffer:
    def __init__(self):
        self.buff = list()

    def add(self, *a):
        self.buff += list(a)
        while len(self.buff) >= 5:
            s = sum(self.buff[:5])
            self.buff = self.buff[5:]
            print(s)

    def get_current_part(self):
        return self.buff

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6) 
print(buf.get_current_part() )
buf.add(7, 8, 9, 10) 
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) 
print(buf.get_current_part() )




class A:
     val = 1
     def foo(self):
             A.val +=10
     def bar(self):
             self.val += 1