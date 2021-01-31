fibo_cache={}

def fibon(n):
    #check if the value is already saved in cache
    if n in fibo_cache:
      return fibo_cache[n]
    if n==1:
      val=1
    elif n==2:
      val=1
    elif n>2:
      val=fibon(n-1)+fibon(n-2)    
    #cache the value and return val
    fibo_cache[n]=val
    return val

#fibon
for n in range(1,101):
    print(n,"=",fibon(n))