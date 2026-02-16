# Positive, Negative or Zero

n = int(input("Enter your number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Biggest of 3 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>=b and a>=c:
    print("Biggest number is:", a)
elif b>=a and b>=c:
    print("Biggest number is:", b)
else:
    print("Biggest number is:", c)
