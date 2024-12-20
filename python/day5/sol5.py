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
        incorrect_updates.append(update) # for part 2 

print(middle_values)

## Part 2 of Day 5 ## 

inc_mid_vals = 0

for update in incorrect_updates: 
    for counter, page in enumerate(update): 
        for i, p in enumerate(update[:counter]): 
            if p in rules[page]: 
                temp1 = update[counter]
                update[counter] = update[i]
                update[i] = temp1

    inc_mid_vals += update[len(update) // 2]

print(inc_mid_vals)