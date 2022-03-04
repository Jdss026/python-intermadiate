"""
Recursion: A function call itself
"""

### NON RECURSIVE WAY ###
'''
n = 5
fact = 1

while n>0:
    fact = fact * n
    n-=1

print(fact)
'''

def factorial(n):
    if n < 1:
        return 1
    else:
        number = n * factorial(n-1)
        return number


def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

def fibonacci2(n):
    if n<=1:
        return n
    else:
        return (fibonacci2(n-1) + fibonacci2(n-2))
    

print(fibonacci(40)) #mais rápido
print(fibonacci2(40)) # mais lento, pois tem custo exponencial
