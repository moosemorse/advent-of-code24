from puzzleInput3 import puzzleInput 

import re

## Part 1 of Day 3 ## 

# regex pattern to match requirements for mul(x,y)
pattern = r"mul\((-?\d+),(-?\d+)\)"

# find all matches in the string
matches = re.findall(pattern, puzzleInput)

total = 0 

for x in matches: 
    total += (int(x[0]) * int(x[1]))

print(total)

## Part 2 of Day 3 ## 


