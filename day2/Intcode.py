program = [int(i) for i in open("input.txt", "r").readline().split(',')]
pos = 0

def add(pos_1, pos_2, dest):
    program[dest] = program[pos_1] + program[pos_2] 

def multiply(pos_1, pos_2, dest):
    program[dest] = program[pos_1] * program[pos_2] 

program[1] = 12
program[2] = 2
while program[pos] != 99:
    if program[pos] == 1:
        add(program[pos + 1], program[pos + 2], program[pos + 3])
    elif program[pos] == 2:
        multiply(program[pos + 1], program[pos + 2], program[pos + 3])
    pos += 4

print(program[0])
