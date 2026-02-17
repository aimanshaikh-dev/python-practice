# Print first character

s = input("Enter a word: ")
print("First character:", s[0])


# Reverse string

s2 = input("Enter a word: ")
print("Reverse:", s2[::-1])


# Count vowels

s3 = input("Enter a string: ")
count = 0
for ch in s3.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:", count)


# Function with return

def add(a, b):
    return a + b
  
print("Add result:", add(3,4))


# lambda

square = lambda x: x * x
print("Square: ", square(5))
