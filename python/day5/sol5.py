from puzzleInput5 import puzzleInput1, puzzleInput2
from collections import defaultdict

## Part 1 of Day 5 ## 

rules = defaultdict(list)
puzzleInput1 = puzzleInput1.split("\n")
puzzleInput2 = puzzleInput2.split("\n")
updates = []
middle_values = 0
incorrect_updates = []

for rule in puzzleInput1:
    rules[int(rule[:2])].append(int(rule[3:])) # dict with rules int : int 

for update in puzzleInput2: 
    temp = update.split(",")
    int_list = [int(s) for s in temp] 
    updates.append(int_list) # list of list of integers for page numbers

for update in updates:
    valid = True 
    for counter, page in enumerate(update): 
        if any(elem in rules[page] for elem in update[:counter]):
            valid = False
    if valid: 
        middle_values += update[len(update) // 2]
    else: 
        incorrect_updates.append(update) 

print(middle_values)

## Part 2 of Day 5 ## 

