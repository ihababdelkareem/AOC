def input():
    return list(map(lambda n: int(n), open('input1.txt').read().split(' ')))

def blink(stone, iterations_left, cache):
    if iterations_left == 0:
        return 1
    if (stone, iterations_left) not in cache:
        if stone == 0:
            cache[(stone, iterations_left)] = blink(1, iterations_left - 1, cache)
        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            cache[(stone, iterations_left)] = blink(int(stone_string[:len(stone_string) // 2]), iterations_left -1, cache) + blink(int(stone_string[len(stone_string) // 2:]), iterations_left -1, cache)
        else:
            cache[(stone, iterations_left)] = blink(stone * 2024, iterations_left - 1, cache)
    return cache[(stone, iterations_left)]
    
def part1():
    cache = dict()
    return sum(blink(stone, 25, cache) for stone in input())

def part1():
    cache = dict()
    return sum(blink(stone, 75, cache) for stone in input())