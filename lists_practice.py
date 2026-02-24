# Create and print a list
numbers = [5 , 10 , 15 , 20 ,25]
print("Lists:", numbers)


# Print first and last element 
print("First element:" , numbers[0])
print("Last element:" , numbers[-1])


# Add an element using append()
numbers.append(30)
print("After append:", numbers)

# Removing an element
numbers.remove(30)
print("After removing 30:", numbers)

# Sort the list
numbers = [11 , 17 , 15 , 2 ,25]
numbers.sort()
print("After sorting:", numbers)


# Checking length of the list
print("Length of lists:", len(numbers)) # Output: 5
