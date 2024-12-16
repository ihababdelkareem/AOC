import re
import os
import time

X,Y = 101, 103

def input_():
    data = []
    pattern = re.compile(r"p=(\d+),(\d+)\s+v=([-]?\d+),([-]?\d+)")
    with open("input1.txt", "r") as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                x, y, dx, dy = map(int, match.groups())
                data.append([x, y, dx, dy])
    return data

def print_(data):
    grid = [[0] * X for _ in range(Y)]
    for x, y, _, _ in data:
        grid[y][x] += 1
    print('-' * 100)
    for row in grid:
        print(''.join(list(map(lambda n: '.' if n == 0 else '*', row))))
    print('X' * 100)

def surroundings(x,y,grid):
    return sum(grid[x + i][y + j] >= 1 for i,j in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)] if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0])) == 6

def part2():
    data = input_()
    grid = [[0] * X for _ in range(Y)]
    for s in range(100000000):
        number_surrounded = sum(surroundings(d[0], d[1], grid) for d in data)
        if number_surrounded >= 3:
            print_(data)
            print(s)
            input()
        for i in range(len(data)):
            grid[data[i][1]][data[i][0]] -= 1
            data[i][0] = (data[i][0] + data[i][2]) % X
            data[i][1] = (data[i][1] + data[i][3]) % Y
            grid[data[i][1]][data[i][0]] += 1
    a,b,c,d = 0,0,0,0
    for x, y, _, _ in data:
        if x < X // 2:
            if y < Y // 2:
                a += 1
            elif y > Y // 2:
                b += 1
        elif x > X // 2:
            if y < Y // 2:
                c += 1
            elif y > Y // 2:
                d += 1
    
    return a * b * c * d