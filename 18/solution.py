from collections import deque

def input():
    grid = [['.'] * 71 for _ in range(71)]
    for j,i in [list(map(int, line.split(','))) for line in open('input1.txt').read().splitlines()]:
        grid[i][j] = '#'
    return grid

def part1():
    grid = input()
    q = deque([(0,0)])
    dist = {(0,0): 0}
    while q:
        i,j = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= i + dx < 71 and 0 <= j + dy < 71 and grid[i+dx][j+dy] != '#' and (i + dx, j + dy) not in dist:
                dist[(i+dx, j+dy)] = dist[(i,j)] + 1
                q.append((i+dx, j+dy))
    return dist[(70,70)]

"""
Binary search the file by hand
"""
def part2():
    pass