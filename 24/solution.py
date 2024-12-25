from collections import deque
OP_MAP = {'AND': lambda x,y: x & y, 'OR': lambda x, y: x | y, 'XOR': lambda x,y: x ^ y}

def input():
    value_map = {}
    for line in open('input1.txt').read().splitlines():
        if ':' in line:
            key, value = line.split(': ')
            value_map[key] = int(value)
        elif '->' in line:
            equation, destination = line.split(' -> ')
            op1, operation, op2 = equation.split(' ')
            value_map[destination] = (op1, operation, op2)
    return value_map

def part1():
    value_map = input()
    resolve_queue = deque()
    for key, value in value_map.items():
        if not isinstance(value,int):
            resolve_queue.append(key)
    while resolve_queue:
        key_to_resolve = resolve_queue.popleft()
        op1,operation,op2 = value_map[key_to_resolve]
        if isinstance(value_map[op1], int) and isinstance(value_map[op2], int):
            value_map[key_to_resolve] = OP_MAP[operation](value_map[op1], value_map[op2])
        else:
            resolve_queue.append(key_to_resolve)
    z_number = []
    for key, value in value_map.items():
        if key[0] == 'z':
            z_number.append((key, value))

    return int(''.join(list(map(lambda x: str(x[1]), sorted(z_number, reverse=True)))),2)

def part2():
    value_map = input()
    incorrect_zs = []
    incorrect_xor_operands = []
    receives_xor_x_y = []
    receives_and_x_y = []
    for key in value_map:
        if isinstance(value_map[key], tuple) and key[0] == 'z' and ((key == 'z45' and value_map[key][1] != 'OR') or (key != 'z45' and value_map[key][1] != 'XOR')):
            incorrect_zs.append(key)
        if isinstance(value_map[key], tuple) and key[0] != 'z' and {value_map[key][0][0], value_map[key][2][0]} != {'x', 'y'} and value_map[key][1] == 'XOR':
            incorrect_xor_operands.append(key)

        if isinstance(value_map[key], tuple) and key[0] != 'z' and {value_map[key][0][0], value_map[key][2][0]} == {'x', 'y'} and {value_map[key][0], value_map[key][2]} != {'x00', 'y00'} and value_map[key][1] == 'XOR':
            receives_xor_x_y.append(key)
        if isinstance(value_map[key], tuple) and key[0] != 'z' and {value_map[key][0][0], value_map[key][2][0]} == {'x', 'y'} and {value_map[key][0], value_map[key][2]} != {'x00', 'y00'} and value_map[key][1] == 'AND':
            receives_and_x_y.append(key)
        

    violates_receiving_xor_x_y = []
    violates_receiving_and_x_y = []
    for test in receives_xor_x_y:
        violates = True
        for key in value_map:
            if isinstance(value_map[key], tuple) and value_map[key][1] == 'XOR' and test in {value_map[key][0],value_map[key][2]}:
                violates = False
                break
        if violates:
            violates_receiving_xor_x_y.append(test)

    for test in receives_and_x_y:
        violates = True
        for key in value_map:
            if isinstance(value_map[key], tuple) and value_map[key][1] == 'OR' and test in {value_map[key][0],value_map[key][2]}:
                violates = False
                break
        if violates:
            violates_receiving_and_x_y.append(test)
    
    return ','.join(list(sorted(incorrect_zs + incorrect_xor_operands + violates_receiving_xor_x_y + violates_receiving_and_x_y)))