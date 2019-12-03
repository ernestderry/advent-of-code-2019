

def executeOptCode(program, pos):
    optCode = program[pos]

    if optCode == 1 :
        program[program[pos+3]] = program[program[pos+1]] + program[program[pos+2]]
    elif optCode == 2 :
        program[program[pos+3]] = program[program[pos+1]] * program[program[pos+2]]


def runProgram(program):
    
    pos = 0

    while program[pos] != 99 :
        executeOptCode(program, pos)
        pos += 4