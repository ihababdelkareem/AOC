from collections import defaultdict
class Key:
    def __init__(self, val, rules) -> None:
        self.val = val
        self.rules = rules
    def __lt__(self, other):
        return other.val in self.rules[self.val]

def input():
    rules = defaultdict(set)
    lists = []
    for line in open('input1.txt').readlines():
        line = line.rstrip('\n')
        if '|' in line:
            small, big = line.split('|')
            small, big = int(small), int(big)
            rules[small].add(big)
        else:
            lists.append(list(map(lambda s: Key(int(s),rules), line.split(','))))
    return lists

def part1():
    return sum(l[len(l) // 2].val for l in input() if l == sorted(l))

def part2():
    return sum(sorted(l)[len(l) // 2].val for l in input() if l != sorted(l))