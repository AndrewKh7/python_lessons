#
#'''
#task 1
#
#'''
#
#n = int(input())
#classes = [input() for i in range(n)] 
#n = int(input())
#requests = [ input().split() for i in range(n)]
#dictionary_of_classes = dict()
#for i in classes:
#    parts_of_cheks = i.split(':')
#    if len(parts_of_cheks) == 1:
#        dictionary_of_classes[i] = []
#    else:
#        dictionary_of_classes[parts_of_cheks[0].strip()] = (parts_of_cheks[-1]).split()
#        for j in dictionary_of_classes[parts_of_cheks[0].strip()]:
#            if j not in  dictionary_of_classes:
#                dictionary_of_classes[j] = []
#
#
#print(dictionary_of_classes)
#
#def is_parent(parent,child):
#    '''
#    This function checks is the <paret> an ancestor of <child>
#    '''
#    if child not in dictionary_of_classes: return False 
#    if parent in dictionary_of_classes[child] or parent == child:
#        return True
#    else:
#        for i in dictionary_of_classes[child]:
#            if is_parent(parent,i):
#                return True
#    return False
#
#
#for parent, child in requests:
#    # print(parent,child, end ='')
#    if is_parent(parent,child):
#        print('Yes')
#    else:
#        print('No')

##'''
##task 2
##
##'''
#class ExtendedStack(list):
#    def sum(self):
#        a = self.pop()
#        b = self.pop()
#        self.append(a+b)
#
#    def sub(self):
#        a = self.pop()
#        b = self.pop()
#        self.append(a-b)
#
#
#    def mul(self):
#        a = self.pop()
#        b = self.pop()
#        self.append(a*b)
#        
#    def div(self):
#        a = self.pop()
#        b = self.pop()
#        self.append(a//b)
#    
#obj = ExtendedStack([1,2,3,4,5])
#obj.sum()
#print(obj[-1])
#
#obj.sub()
#print(obj[-1])
#
#obj.mul()
#print(obj[-1])
#
#obj.div()
#print(obj[-1])

##'''
##task 3
##
##'''
import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
class LoggableList(list,Loggable):
    def append(self,item):
       self.log(item)
       super(LoggableList,self).append((item))
       
obj = LoggableList()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)
