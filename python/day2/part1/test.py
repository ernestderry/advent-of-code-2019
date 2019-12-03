import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))


program = [1,0,0,0,99]
main.runProgram(program)
assertEquals(1, [2,0,0,0,99], program)

program = [2,3,0,3,99]
main.runProgram(program)
assertEquals(1, [2,3,0,6,99], program)

program = [2,4,4,5,99,0]
main.runProgram(program)
assertEquals(1, [2,4,4,5,99,9801], program)

program = [1,1,1,4,99,5,6,0,99]
main.runProgram(program)
assertEquals(1, [30,1,1,4,2,5,6,0,99], program)

f = open("python/day2/puzzle.txt", "r")
program = list(map(int, f.readline().split(",")))
program[1] = 12
program[2] = 2
main.runProgram(program)

print ("the answer is " + str(program[0]))









