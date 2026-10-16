marks = [78, 92, 55, 88, 67, 95, 81, 45, 73, 90]
students = ["Aarav", "diya", "Kabir", "Meera", "rohan", "Isha", "Vivaan", "sara", "arjun", "Zoya"]

# sorted(list)
# returns a new sorted list and does not change the original list
new_list = sorted(marks) # [45, 55, 67, 73, 78, 81, 88, 90, 92, 95]
print(new_list)
print(marks) # [78, 92, 55, 88, 67, 95, 81, 45, 73, 90]

# list.sort()
# sorts the list in place and returns None
# changes the original list
sort_list = marks.sort() # [45, 55, 67, 73, 78, 81, 88, 90, 92, 95] # None
print(sort_list) # None
print(marks.sort()) # None
print(marks) # [45, 55, 67, 73, 78, 81, 88, 90, 92, 95]

print(sorted(students)) # ['Aarav', 'Isha', 'Kabir', 'Meera', 'Vivaan', 'Zoya', 'arjun', 'diya', 'rohan', 'sara']
print(sorted(students, key=str.upper)) # ['Aarav', 'arjun', 'diya', 'Isha', 'Kabir', 'Meera', 'rohan', 'sara', 'Vivaan', 'Zoya']
print(sorted(students, key=str.lower, reverse=True)) # ['Zoya', 'Vivaan', 'Sara', 'Rohan', 'Meera', 'Kabir', 'Isha', 'Diya', 'arjun', 'Aarav']