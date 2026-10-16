# MINI CODING PROJ - STUDENT RESULT ANALYZER
# Store marks of students in a list
# Find highest & lowest marks
# Calculate the Avg
# Count students scoring above 80
# Accepts a student's name & check whether it exists
# Sort and print top 3 marks
# show each name with its marks using enumerate()
# assign grades(A/B/C) by range
# Display neatly 

marks = [78, 92, 55, 88, 67, 95, 81, 45, 73, 90]
names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Isha", "Vivaan", "Sara", "Arjun", "Zoya"]

def result_analyzer(marks, names, search_name):
    # highest marks
    highest = max(marks)
    # lowest marks
    lowest = min(marks)
    # avg
    avg = sum(marks) // len(marks) # avg = (sum of obser) / (total no.of obser)
    # no.of students count who scored above 80 using list comprehension
    scored_above_80 = sum(1 for mark in marks if mark>80)

    # using for loop
    """
    scored_above_80 = 0
    for m in marks:
        if m>80
        return scored_above_80 += 1
    """
    # check whether the name is present in list 
    clean_serach = search_name.lower().strip()
    clean_name = [name.lower().strip() for name in names]
    found = clean_serach in clean_name

    # top 3 marks from the list
    top_3_marks = sorted(marks)

    print("="  * 30)
    print(" STUDENT RESULT ANALYZER")
    print("="  * 30)
    print(f"Total Students : {len(names)}")
    print(f"Highest Marks : {highest}")
    print(f"lowest Marks : {lowest}")
    print(f"Average Marks : {avg}")
    print(f"Scored above 80 : {scored_above_80}")
    print(f"{search_name.strip()} found? : {found}")
    print(f"Top 3 marks : {top_3_marks[7:]}")
    print("-"  * 30)
    print("Students Score & Grade")
    print("-"  * 30)
    # show each name with its marks using enumerate()
    for index, name in enumerate(names):
        score = marks[index]
        # assign grades(A/B/C) by range
        if score>=85:
            grade = "A"
        elif score>=65:
            grade = "B"
        else:
            grade = "C"
        print(f"{index + 1}. {name} scored {score} | grade : {score}")
    print("-"  * 30)
    print("="  * 30)

result_analyzer(marks, names, "  diya  ")