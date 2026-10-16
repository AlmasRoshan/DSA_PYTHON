# TRAVERSING A DICTIONARY

stu = {
    "name": "John",
    "age": 25,
    "city": "New York"
    }

# Loop through the keys of the dictionary (by default the loop iterates over the keys)
for key in stu:  
    print(key, end=" ")  # Print the key followed by a space
print()  # Print a newline after traversing the keys

# Loop through the values of the dictionary
for val in stu.values():
    print(val, end=" ")  # Print the value followed by a space
print()  # Print a newline after traversing the values

# Loop through the key-value pairs of the dictionary
for key, val in stu.items():
    print(f"{key}: {val}")  # Print the key and value in the format "key: value"