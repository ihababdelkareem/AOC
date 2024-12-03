import re
def input():
    return open('input1.txt').read()

def part1():
    print(sum(x * y for x,y in map(lambda str: tuple(map(int, str[4:-1].split(','))), re.findall(r'mul\(\d+,\d+\)',input()))))

def part2():
    in_ = input()
    mul_with_start = [(match.start(), match.group()) for match in re.finditer(r'mul\(\d+,\d+\)', in_)]
    do_dont = [(match.start(), match.group()) for match in re.finditer(r"\b(?:do|don't)\b", in_)]
    combined = list(map(lambda x: x[1], sorted(do_dont + mul_with_start, key = lambda x: x[0])))
    do = True
    res = 0
    for term in combined:
        if term == 'do':
            do = True
        elif term == "don't":
            do = False
        elif do:
            x, y = tuple(map(int, term[4:-1].split(',')))
            res += x * y