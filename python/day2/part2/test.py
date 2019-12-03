import main

f = open("python/day2/puzzle.txt", "r")
originalProgram = list(map(int, f.readline().split(",")))

foundAnswer = False
for noun in range(100):
    for verb in range(100):       
        program = originalProgram.copy()
        program[1] = noun
        program[2] = verb
        main.runProgram(program)
        if program[0] == 19690720:
            foundAnswer = True
        if foundAnswer : break
    if foundAnswer : break

print("the answer is " + str(100*noun+verb))










