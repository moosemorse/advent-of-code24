from puzzleInput6 import puzzleInput

puzzleInput = puzzleInput.split("\n") 

def find_guard(input): 
    for row in input: 
        for c in row: 
            if c == "^": 
                return (row, c) 
            
orientation = 90 # starting orientation pointing up 
xCount = 0 
lastElem = "#"
currPos = find_guard(puzzleInput)

while (lastElem != "."): 
    
    if orientation == 90:  
        for i in range()

    if orientation == 180: 

    if orientation == 270: 

    if orientation == 0: 
    
    orientation = (orientation - 90) % 360 