def input():
    return [list(map(int, line.rstrip('\n').split(' '))) for line in open('input1.txt').readlines()]

def is_safe(list_):
    deltas = list(zip(list_[1:], list_[:-1]))
    max_diff, min_diff = max(high - low for high, low in deltas), min(high - low for high, low in deltas)
    return (1 <= min_diff and max_diff <= 3) or (-1 >= max_diff and min_diff >= -3)

def part1():
    print(sum(int(is_safe(list_)) for list_ in input()))

def part2():
    print(sum(int(any((is_safe(list_[:i] + list_[i+1:]) for i in range(len(list_))))) for list_ in input()))