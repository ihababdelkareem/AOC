def input():
    return list(map(lambda line: list(map(lambda char: int(char), line.rstrip('\n'))), open('input1.txt').readlines()))

def dfs(grid, i, j, visited, unique):
    visited |= ({(i,j)} if unique else set())
    if grid[i][j] == 9:
        return 1
    return sum(dfs(grid, i + dx, j + dy, visited, unique) for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and grid[i + dx][j + dy] == grid[i][j] + 1 and (i+dx, j+dy) not in visited)
    
def part1():
    grid = input()
    return sum([dfs(grid, i,j, set(), True) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0])

def part2():
    grid = input()
    return sum([dfs(grid, i,j, set(), False) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 0])