# MINI CODING PROJECT - STUDENT RANKING SYSTEM
# Searching and Sorting together in a single program
# stores students names and marks
# sorts students by marks (highest to lowest) to make a ranking
# finds a student with Linear Search (by name)
# finds a mark with Binary Search (after sorting the marks)
# display the topper and lowest score

students = [
    ["Aarav", 78],
    ["Diya", 92],
    ["Kabir", 55],
    ["Meera", 88],
    ["Rohan", 67]
]

def ranking(students):
    # sorting marks in desc order
    # key=lambda s: s[1] --> picking index[0], i.e is marks form each student in the list 
    return sorted(students, key=lambda s: s[1], reverse=True)


def linear_search(students, name):
    for student in students:
        # student[0] --> index[0] of all students, i.e is only names
        if student[0].lower() == name.strip().lower():
            return student
    return None

def binary_search(sorted_marks, target):
    low, high = 0, len(sorted_marks) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_marks[mid] == target:
            return mid
        elif sorted_marks[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return -1

# calling ranking function (function call)
ranks_list = ranking(students)
# picking index[1], i.e is marks form each student in the list
# as binary search only accepts sorted data
sorted_marks = sorted([s[1] for s in students])

# print statements
print("=" * 40)
print("     STUDENT RANKING SYSTEM")
print("=" * 40)
# <4 are spacing --> < spacing to the left and > spacing to the right
print(f"{'Rank':<4} | {'Name':<6} | {'Marks':<4}")
for rank, (name, mark) in enumerate(ranks_list, start=1):
    print(f"{rank:<4} | {name:<6} | {mark:<4}") 

print("-" * 40)
print(f"Topper: {ranks_list[0][0]} ({ranks_list[0][1]})")
print(f"Lowest Score: {ranks_list[-1][0]} ({ranks_list[-1][1]})")
print(f'''Linear Search 'meera': {linear_search(students, "meera")}''')
print(f"Binary Search Mark 88: index {binary_search(sorted_marks, 88)} in {sorted_marks}")
print("=" * 40)
