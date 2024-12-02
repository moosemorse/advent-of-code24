from puzzleInput2 import puzzleInput 

parsedInput = [[int(x) for x in line.split()] 
               for line in puzzleInput.split("\n")]

## Part 1 of Day 2 ## 

safe_counter = len(parsedInput) # decrement if row not safe

for row in parsedInput: 
    if row == sorted(row) or row == sorted(row, reverse=True): 
        for x in range(len(row)-1): 
            if abs(row[x] - row[x+1]) < 1 or abs(row[x] - row[x+1]) > 3:
                safe_counter -= 1 
                break
    else: 
        safe_counter -= 1

print(f"Part 1: {safe_counter}")

## Part 2 of Day 2 ## 

def check_row(row): 

    if row == sorted(row) or row == sorted(row, reverse=True):
        for x in range(len(row) - 1): 
            if abs(row[x] - row[x+1]) < 1 or abs(row[x] - row[x+1]) > 3: 
                return False
    else: 
         return False
    
    return True 
    
    

safe_counter= len(parsedInput) 

for row in parsedInput: 
    safe = False
    
    if check_row(row) == True: 
        safe = True 

    else: 
        for i in range(len(row)): 
            modified_row = row[:i] + row[i+1:]
            if check_row(modified_row) == True: 
                safe = True 
                break

    if safe == False: 
        safe_counter -= 1

print(f"Part 2: {safe_counter}")