##'''
##tsak 1
##,,,
#n = int(input())
#exceptions = [input() for i in range(n)]
#dict_of_ex = dict()
#for ex in exceptions:
#    v = ex.split(':')
#    if len(v) == 1 :
#        dict_of_ex[v[0].strip()] = []
#    else:
#        dict_of_ex[v[0].strip()] = v[-1].split()
#        for k in dict_of_ex[v[0].strip()]:
#            if k not in dict_of_ex:
#                dict_of_ex[k] = []
#
#m = int(input())
#try_ex = [input().strip() for i in range(m)]
#
#set_of_checked_except = set()
#def it_was(item):
#    '''
#    This function checks an item has been processed
#
#    '''
#    if item in set_of_checked_except: return True
#    for i in dict_of_ex[item]:
#        if i in set_of_checked_except:
#            return True
#        else:
#            return it_was(i)
#    return False
#
#for i in try_ex:
#    if it_was(i):
#        print(i)
#        continue
#    set_of_checked_except.add(i)
#    

#'''
#task 2
#,,,

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self,x):
        if x<=0:
            raise NonPositiveError(str(x) + ' is not positive')
        else:
            super(PositiveList,self).append(x)
l = PositiveList()
l.append(-2)
