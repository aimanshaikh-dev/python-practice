# Creating a tuple
 
t = (10, 20, 20, 30, 40)

print("Tuple:", t)
print("First element:", t[0])
print("Last eleement:", t[-1])
print("Lenght:", len(t))

# Count and Index

print("Count of 20:", t.count(20))
print("index of 30:", t.index(30))

# Create sets

a ={1, 2, 3, 4}
b ={3, 4, 5, 6}

print("Set A:", a)
print("Set b:", b)

# Union , Intersection , Difference

print("Union of:", a.union(b))
print("Intersection of:", a.intersection(b))
print("Difference of:", a.difference(b))

# Add and Remove

a.add(7)
a.remove(4)
print("Updated A:", a)
