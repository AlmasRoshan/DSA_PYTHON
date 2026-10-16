# DICTIONARY OPERATIONS

stu = {
    "name": "John",
    "age": 25,
    "city": "New York"
    }

# ACCESS - read a val by key
print(stu["name"])  # Output: John

# UPDATE - change an existing val by key
stu["age"] = 26
print(stu["age"])  # Output: 26

# ADD - add a new key-value pair
stu["country"] = "USA"
print(stu["country"])  # Output: USA
print(stu)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'country': 'USA'}

# DELETE - remove a key-value pair by key
del stu["city"]
print(stu)  # Output: {'name': 'John', 'age': 26, 'country': 'USA'}

#---------------------------------------------------------------------------------------------------------------------

# BUILT -IN METHODS IN DICTIONARY

print(stu.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(stu.values())  # Output: dict_values(['John', 26, 'USA'])
print(stu.items())  # Output: dict_items([('name', 'John'), ('age', 26), ('country', 'USA')])

# get() - safe access, no crash if key doesn't exist
# get(key, default_val) - if key exists, return its value; if not, return default_val (if provided) or None (if not provided)
print(stu.get("name"))  # Output: John
print(stu.get("name", "Not Found"))  # Output: John
print(stu.get("gender")) # Output: None
print(stu.get("gender", "Not Found"))  # Output: Not Found

# pop() - remove a key-value pair by key and return its value; if key doesn't exist, raise KeyError
removed = stu.pop("age")
print(removed)  # Output: 26
print(stu)  # Output: {'name': 'John', 'country': 'USA'}

# copy() - create a shallow copy of the dictionary
stu_copy = stu.copy()

# clear() - remove all key-value pairs from the dictionary and return an empty dictionary
stu.clear()
print(stu)  # Output: {}
print(stu_copy)  # Output: {'name': 'John', 'country': 'USA'}