def input_():
    registers = {}
    instructions = []
    lines = open('input1.txt').read().splitlines()
    registers['A'] = int(lines[0].split(':')[1].strip())
    registers['B'] = int(lines[1].split(':')[1].strip())
    registers['C'] = int(lines[2].split(':')[1].strip())
    instructions = list(map(int,lines[4].split(':')[1].strip().split(',')))
    return instructions, registers

def resolve_combo_operand(operand, registers):
    combo_register = {4:'A',5:'B',6:'C'}
    if operand <= 3:
        return operand
    return registers[combo_register[operand]]

def run_program(instructions, registers):
    ip = 0
    out = []
    while ip < len(instructions):
        instruction = instructions[ip]
        jump = False
        if instruction == 0:
            registers['A'] = registers['A'] // (1 << resolve_combo_operand(instructions[ip + 1],registers))
        elif instruction == 1:
            registers['B'] = registers['B'] ^ instructions[ip + 1]
        elif instruction == 2:
            registers['B'] = resolve_combo_operand(instructions[ip + 1], registers) % 8
        elif instruction == 3:
            if registers['A'] != 0:
                ip = instructions[ip + 1]
                jump = True
        elif instruction == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif instruction == 5:
            out.append(resolve_combo_operand(instructions[ip + 1],registers) % 8)
        elif instruction == 6:
            registers['B'] = registers['A'] // (1 << resolve_combo_operand(instructions[ip + 1],registers))
        elif instruction == 7:
            registers['C'] = registers['A'] // (1 << resolve_combo_operand(instructions[ip + 1],registers))
        if not jump:
            ip += 2
    return out

def part1():
    return ','.join(map(str,run_program(*input_())))

def part2():
    def backtrack(instructions, target_octal_index, candidate_number):
        if target_octal_index == -1:
            return candidate_number
        else:
            for test in range(8):
                if run_program(instructions, {'A': (candidate_number << 3) | test,'B':0,'C':0})[0] == instructions[target_octal_index]:
                    solution = backtrack(instructions, target_octal_index - 1, (candidate_number << 3) | test)
                    if solution != -1:
                        return solution
        return -1
    instructions = input_()[0]
    return backtrack(instructions, len(instructions) - 1, 0)