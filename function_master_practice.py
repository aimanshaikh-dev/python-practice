# Even or Odd (using return)

def even_or_odd(n): 
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print("Even or Odd:", even_or_odd(8))


# Biggest of 3 numbers (without max())

def biggest(a,b,c):
    if a>=b and a>=c:
        return a
    if b>=a and b>=c:
        return b
    else:
        return c
      
print("Biggest:" , biggest(10, 20, 30))


# Factorial usinf recursion

def factorial(n):
    if n == 2:
        return 1
    return n * factorial(n-1)

print("Factorial:", factorial(2))


# lambda function

square  = lambda x: x*x
print("Square:", square(5))


# Using math Module

import math
print(math.sqrt(16))


# Variable scope example

x =10 #Global variable

def show_scope():
    x = 6 #Local variable
    print("Inside function:", x)

show_scope()
print("Outside function:", x)
