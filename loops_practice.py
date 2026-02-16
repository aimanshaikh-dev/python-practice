# Print numbers from 1 to 10

for i in range(1,11):
    print(i)


# Print even numbers from 1 to 20

for i in range(1,21):
    if i % 2 == 0:
        print(i)


# Sum of first 10 numbers

total  = 0

for i in  range(1,11):
    total += i

print("Sum is:", total)


# Multiplication table

n = int(input("Enter a number: "))

for i in range(1,11):
    print(n , "X", i, "=", n * i)
