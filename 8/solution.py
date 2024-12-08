from collections import defaultdict
def input():
    return list(map(lambda line: list(line.rstrip('\n')), open('input1.txt').readlines()))

def generate_antennas(p1,p2,m,n,any_position=False):
    x1,y1,x2,y2 = *p1, *p2
    dx,dy = x2 - x1, y2 - y1
    res_1, res_2 = [], []
    while 0 <= x2 < m and 0 <= y2 < n:
         res_1.append((x2,y2))
         x2 += dx
         y2 += dy
    x1,y1,x2,y2 = *p1, *p2
    while 0 <= x1 < m and 0 <= y1 < n:
         res_2.append((x1,y1))
         x1 -= dx
         y1 -= dy
    if not any_position:
         return ([res_1[1]] if len(res_1) > 1 else []) + ([res_2[1]] if len(res_2) > 1 else [])
    return res_1 + res_2

def count_locations(any_position=False):
    freq_locations, grid = defaultdict(list), input()
    m,n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '.':
                freq_locations[grid[i][j]].append((i,j))
    res = set()
    for _,freq_positions in freq_locations.items():
        for p1 in range(len(freq_positions)):
            for p2 in range(p1 + 1, len(freq_positions)):
                    res |= set(generate_antennas(freq_positions[p1],freq_positions[p2],m,n,any_position))
    return len(res)

def part1():
     return count_locations(False)

def part2():
    return count_locations(True)