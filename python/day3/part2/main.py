def plotLine(lineNumber, instructions, grid):
    x = 0
    y = 0
    stepsFromOrigin = 0
    if instructions != "":
        for instruction in instructions.split(","):
            instruction = instruction.strip()
            direction = instruction[0:1]
            distance = int(instruction[1:])
            for steps in range(distance):
                stepsFromOrigin += 1

                if direction == "L":
                    x -= 1
                elif direction == "R":
                    x += 1
                elif direction == "U":
                    y += 1
                else:
                    y -= 1

                if x != 0 or y != 0 :
                    if (x,y) in grid:
                        crossingLinesAtGridPosition = grid[(x,y)]
                        lineBeenHereBefore = False
                        for line in crossingLinesAtGridPosition:
                            if line[0] == lineNumber:
                                lineBeenHereBefore = True
                                stepsFromOrigin = line[1]

                        if not lineBeenHereBefore:
                            grid[(x,y)].append([lineNumber, stepsFromOrigin])
                    else:                        
                        grid[(x,y)] = [[lineNumber, stepsFromOrigin]]

def buildGrid(line1Instructions, line2Instructions):

    x = 0
    y = 0
    grid = {}
    plotLine(1, line1Instructions, grid)
    plotLine(2, line2Instructions, grid)

    return grid


def findNearestCrossedPath(grid):
    shortestDistance = 9999
    for key in grid.keys():
        crossingLinesAtGridPosition = grid[key]
        if len(crossingLinesAtGridPosition) > 1 :
            totalSteps = crossingLinesAtGridPosition[0][1] + crossingLinesAtGridPosition[1][1]
            if totalSteps < shortestDistance:
                shortestDistance = totalSteps

    return shortestDistance


def visualizeGrid(grid):
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for key in grid.keys():
        if key[0] < minX :
            minX = key[0]
        if key[0] > maxX :
            maxX = key[0]
        if key[1] < minY :
            minY = key[1]
        if key[1] > maxY :
            maxY = key[1]
    
    for y in range(maxY, minY - 1, -1):
        line = ""
        for x in range(minX, maxX + 1):
            if x==0 and y==0:
                line += "*"                
            elif (x,y) in grid:
                if len(grid[(x,y)]) > 1 :
                    line += "X"
                else:
                    line += str(grid[(x,y)][0])
            else:
                line += " "
        print(line)
        
