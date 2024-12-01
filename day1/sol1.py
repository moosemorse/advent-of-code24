from puzzleInput1 import puzzleInput

## Part 1 of Day 1 ## 

parsedInput = puzzleInput.split()
left = sorted([int(x) for x in parsedInput[::2]])
right = sorted([int(x) for x in parsedInput[1::2]])

total_distance = 0 

for i in range(len(left)): 
    total_distance += (abs(left[i] - right[i]))

print(total_distance)

## Part 2 of Day 1 ## 

similarity_score = 0 

for i in range(len(left)): 
    similarity_score += (left[i] * right.count(left[i]))

print(similarity_score)