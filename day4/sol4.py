from puzzleInput4 import puzzleInput
import numpy as np
import re

## Part 1 of Day 4 ## 

# String representation for each row 

rows = puzzleInput.split("\n")

def list_of_rows(rows): # for diagonal subroutine
    
    lst = [] 
    for row in rows: 
        temp = []
        for c in range(len(row)): 
            temp.append(row[c])
        lst.append(temp)
    return lst 

# String representation of each col 

cols = []

for c in range(len(rows[0])): 
    temp = ""
    for row in rows:
        temp += row[c]
    cols.append(temp)

def get_all_diagonals(rows):
    rows = np.array(list_of_rows(rows))
    diagonals = []
    n, m = rows.shape
    
    # Main diagonals (top-left to bottom-right)
    for i in range(-n + 1, m):
        diag = np.diagonal(rows, offset=i)
        if diag.size > 0: 
            diagonals.append(diag)
        diag = np.diagonal(np.fliplr(rows), offset=i)
        if diag.size > 0: 
            diagonals.append(diag)
        
    return diagonals

diags = get_all_diagonals(rows)

# Concatenate each diagonal into a string
diags = [''.join(diag) for diag in diags]

total_string = diags + rows + cols 

total = 0 

for s in total_string: 
    # regex pattern to match requirements for XMAS
    patterns = [r"XMAS", r"SAMX"] 
    
    for pattern in patterns: 
        # find all matches in the string
        matches = re.findall(pattern, s)
        for match in matches: 
            total += 1
            
print(total)
