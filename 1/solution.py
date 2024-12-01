from collections import defaultdict

def part1():
    res = [tuple(map(int, line.rstrip('\n').split('   '))) for line in open('input1.txt').readlines()]
    l1, l2 = [], []
    for left, right in res:
        l1.append(left)
        l2.append(right)
    l1.sort()
    l2.sort()
    print(sum(abs(x - y) for x,y in zip(l1,l2)))

def part2():
    res = [tuple(map(int, line.rstrip('\n').split('   '))) for line in open('input1.txt').readlines()]
    l1, l2 = [], defaultdict(int)
    for left, right in res:
        l1.append(left)
        l2[right] += 1

    print(sum(x * l2[x] for x in l1))