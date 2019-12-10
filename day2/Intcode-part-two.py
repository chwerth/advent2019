from itertools import product

def add(pos_1, pos_2, dest):
    program[dest] = program[pos_1] + program[pos_2] 

def multiply(pos_1, pos_2, dest):
    program[dest] = program[pos_1] * program[pos_2] 

for x, y in product(range(99), range(99)):
    program = [int(i) for i in open("input.txt", "r").readline().split(',')]
    pos = 0
    program[1] = x
    program[2] = y
    while program[pos] != 99:
        if program[pos] == 1:
            add(program[pos + 1], program[pos + 2], program[pos + 3])
        elif program[pos] == 2:
            multiply(program[pos + 1], program[pos + 2], program[pos + 3])
        pos += 4

    if program[0] == 19690720:
        print("noun: " + str(x) + " verb: " + str(y))
        print("Answer: " + str((100 * x) + y))
        break
