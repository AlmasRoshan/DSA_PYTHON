# MINI CODING PROJ - SCHOOL ORGANIZATION MANAGEMENT SYS
# combine a TREE & a HEAP in one prog:
# builds a school hierarchy as a tree (Principal -> Departments -> Teachers)
# stores stu MARKS IN MIN HEAP
# find the stu with the LOWEST marks (heap top)
# displays the TOP-PERFORMING stu's(heapq.nlargest)

import heapq
from collections import deque

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child_node):
        self.children.append(child_node)

principal = TreeNode("Principal")
cs = TreeNode("CS Department")
maths = TreeNode("Maths Department")
principal.add(cs)
principal.add(maths)
cs.add(TreeNode("Mr. Zack (Py Lang)"))
cs.add(TreeNode("Ms. Emma (JS Lang)"))
maths.add(TreeNode("Mr. Bob (stats)"))

def display_hierachy(root):
    queue = deque([(root, 0)])
    while queue:
        node, level = queue.popleft()
        print("  " * level + "- " + node.name)
        for child in node.children:
            queue.append((child, level + 1))
print("SCHOOL HIERARCHY:")
display_hierachy(principal)

marks = [78, 92, 55, 88, 67]
heapq.heapify(marks)
print("Lowest Marks:", marks[0])
print("Top 3 Marks:", heapq.nlargest(3, marks)) # heapq.nlargest(n, var_name)
print("Lowest 2 Marks:", heapq.nsmallest(2, marks))