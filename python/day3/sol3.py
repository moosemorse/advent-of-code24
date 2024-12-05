from puzzleInput3 import puzzleInput 

import re

## Part 1 of Day 3 ## 

def findMul(s):
    # regex pattern to match requirements for mul(x,y)
    pattern = r"mul\((\d+),(\d+)\)"

    # find all matches in the string
    matches = re.findall(pattern, s)

    total = 0 

    for x in matches: 
        total += (int(x[0]) * int(x[1]))

    return total

## Part 2 of Day 3 ## 

doPuzzle = puzzleInput.split("do()")

total = 0 

for x in doPuzzle: 
    total += findMul(x.split("don't()")[0])

print(total)
