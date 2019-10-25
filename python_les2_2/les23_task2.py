
    
def primes():
    last = 1
    cnt = 2
    while 1:
        last+=1
        while cnt<last//2+1:
            if last % cnt == 0:
                last += 1
                cnt = 1
            cnt +=1 
        yield last
        


    

a = primes2()
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
print(next(a))       
