import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))


line1 = "R1"
line2 = ""
expectedGrid = {(1,0):[[1,1]]}
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "R1, R1"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]]}
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "R3, R1"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]], (3,0):[[1,3]], (4,0):[[1,4]] }
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "L2, L1"
line2 = ""
expectedGrid = {(-1,0):[[1,1]], (-2,0):[[1,2]], (-3,0):[[1,3]] }
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "U2, U1"
line2 = ""
expectedGrid = {(0,1):[[1,1]], (0,2):[[1,2]], (0,3):[[1,3]] }
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "D3, D1"
line2 = ""
expectedGrid = {(0,-1):[[1,1]], (0,-2):[[1,2]], (0,-3):[[1,3]], (0,-4):[[1,4]] }
assertEquals("", expectedGrid, main.buildGrid(line1, line2))

line1 = "R2, U2, L2, D1"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]], (2,1):[[1,3]], (2,2):[[1,4]], (1,2):[[1,5]], (0,2):[[1,6]], (0,1):[[1,7]]}
assertEquals("mixed directions", expectedGrid, main.buildGrid(line1, line2))

line1 = "R2, U2, L2, D3"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]], (2,1):[[1,3]], (2,2):[[1,4]], (1,2):[[1,5]], (0,2):[[1,6]], (0,1):[[1,7]], (0,-1):[[1,9]]}
assertEquals("pass through 0,0", expectedGrid, main.buildGrid(line1, line2))

line1 = "R2, U2, L1, D3"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]], (2,1):[[1,3]], (2,2):[[1,4]], (1,2):[[1,5]], (1,1):[[1,6]], (1,-1):[[1,2]]}
assertEquals("pass through itself", expectedGrid, main.buildGrid(line1, line2))

line1 = "R1, U1, L1, D1, R1, U1, L1, D1"
line2 = ""
expectedGrid = {(1,0):[[1,1]], (1,1):[[1,2]], (0,1):[[1,3]]}
assertEquals("go round itself", expectedGrid, main.buildGrid(line1, line2))

line1 = ""
line2 = "R2, U2, L1, D3"
expectedGrid = {(1,0):[[2,1]], (2,0):[[2,2]], (2,1):[[2,3]], (2,2):[[2,4]], (1,2):[[2,5]], (1,1):[[2,6]], (1,-1):[[2,2]]}
assertEquals("line 2", expectedGrid, main.buildGrid(line1, line2))

line1 = "R2, U2"
line2 = "U1, R4"
expectedGrid = {(1,0):[[1,1]], (2,0):[[1,2]], (2,1):[[1,3],[2,3]], (2,2):[[1,4]], (0,1):[[2,1]], (1,1):[[2,2]], (3,1):[[2,4]], (4,1):[[2,5]]}
assertEquals("line 2 crosses line 1", expectedGrid, main.buildGrid(line1, line2))

grid = {(1,0):[[1,1]], (3,3):[[1,2],[2,2]], (2,1):[[1,1],[2,1]], (2,2):[1], (0,1):[2], (1,1):[2], (4,1):[[1,4],[2,4]], (4,1):[2]}
assertEquals("find shortest", 2, main.findNearestCrossedPath(grid))

line1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
line2 = "U62,R66,U55,R34,D71,R55,D58,R83"
grid = main.buildGrid(line1, line2)
assertEquals("example 1", 610, main.findNearestCrossedPath(grid))

line1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
line2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
grid = main.buildGrid(line1, line2)
assertEquals("example 2", 410, main.findNearestCrossedPath(grid))

f = open("python/day3/puzzle.txt", "r")
line1 = f.readline()
line2 = f.readline()
grid = main.buildGrid(line1, line2)
print("the answer is " + str(main.findNearestCrossedPath(grid)))
