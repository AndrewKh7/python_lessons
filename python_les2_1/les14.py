# '''
# Task: Program can create namespacein anather namespace, add variable to namespace and get a namespace when variable stay.
# input:
# first line: number of comands
# Ather lines: comands
# format comand:
# create <namespace> <parent> –  create new namespace with name <namespace> into <parent>
# add <namespace> <var> – add variable into <namespace> with name <var>
# get <namespace> <var> – get namespace where <var> stay or 'None' if it not found
# '''

n = int(input())
com = []

for i in range(n):
    com.append(input().split())

name_spaces ={
                'global': {
                        'parent' : '',
                        'var'  : set()
                        }
            }

def create(parent,names):
    name_spaces[names] = {
                        'parent': parent,
                        'var': set()
                        }
def add(names,var):
    name_spaces[names]['var'].add(var)

def get(names,var):
    if var in name_spaces[names]['var']:
        return names
    else:
        if name_spaces[names]['parent'] == '':
            return 'None'
        else:
            return get(name_spaces[names]['parent'],var)

for i in com:
    if i[0] == 'create':
        create( i[2],i[1] )
    elif i[0] == 'add':
        add( i[1],i[2] )
    elif i[0] == 'get':
        print(get( i[1],i[2] ))
