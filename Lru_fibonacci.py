#recursion implementation using inbuilt memoization
from functools import lru_cache
@lru_cache(maxsize=100)
def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibo(n-1)+fibo(n-2)

for n in range(1,101):
    print(n,"=",fibo(n))