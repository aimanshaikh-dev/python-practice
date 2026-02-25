# Create dictionary
student = {
    "name": "Aiman",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

# Access value
print("Name:", student["name"])

# Add new key
student["city"] = "Bangalore"

# Update value
student["age"] = 21

# Loop through dictonary
for key, value in student.items():
    print(key, ":", value)

