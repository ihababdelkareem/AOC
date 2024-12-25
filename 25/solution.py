def input():
    keys, locks = [], []
    lines = [line for line in open('input1.txt').read().splitlines() if line != '']
    for line_index in range(0, len(lines), 7):
        current_key_or_lock = [0] * 5
        for chunk_line in lines[line_index + 1: line_index + 6]:
            for i in range(len(chunk_line)):
                current_key_or_lock[i] += chunk_line[i] == '#'
        if lines[line_index][0] == '#':
            locks.append(current_key_or_lock)
        else:
            keys.append(current_key_or_lock)
    return locks, keys

def part1():
    locks, keys = input()
    return sum(all(key[i] + lock[i] <= 5 for i in range(5)) for key in keys for lock in locks)