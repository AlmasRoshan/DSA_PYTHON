# MINI CODING PROJECT - STUDENT RECORD MANAGEMENT SYS

# combine a Dict(for records) and a Set(for unique club memebers) in one prog that:
# stores stu details in a Dict (roll num -> details)
# SERACHES a stu by roll num
# UPDATES a stu record
# DEL a record
# DISPLAYS all records 
# maintains a set of unique club members (no duplicates)

class StudentRecords:
    def __init__(self):
        self.records = {}
        self.club_mem = set()

    # to add stu in records
    def add_stu(self, roll_num, name, marks):
        self.records[roll_num] = {"name": name, "marks": marks}
        print(f"Added: {roll_num} -> {name}")

    # to search by roll num
    def search(self, roll_num):
        return self.records.get(roll_num, "NOT FOUND")

    # to update marks by roll num
    def update(self, roll_num, marks):
        if roll_num in self.records:
            self.records[roll_num]["marks"] = marks

    # to del the entire data of a particular stu by roll num
    def delete(self, roll_num):
        if roll_num in self.records:
            del self.records[roll_num]

    # to add names of the stu in the set() - ignores duplicates
    def join_club(self, name):
        self.club_mem.add(name)

    # to display all the stu's 
    def display(self):
        for roll_num, info in self.records.items():
            print(f'{roll_num}: {info["name"]} ({info["marks"]} marks)')

db = StudentRecords()
# adding stu's
db.add_stu(101, "Almas", 37)
db.add_stu(102, "Roshan", 73)
db.add_stu(103, "Afra", 40)

# search by roll num
print("Search 102:", db.search(102)) # roll num present: returns the details present with the roll num
print("Serach 107:", db.search(107)) # roll num not present: returns NOT FOUND as it is the default_val in get()
db.update(103, 80) 
db.delete(101)
print("ALL RECORDS:")
db.display()    # display all the stu's
for name in ["Afra", "Anju", "Afra", "Roshan"]:
    db.join_club(name)
print("Club Members:", sorted(db.club_mem))
