def input():
    return list(map(lambda l: list(l.rstrip('\n')), open('input1.txt').readlines()))

def dfs1(i,j,visited, grid):
    visited.add((i,j))
    area, perimeter = 1,4
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and grid[i+dx][j+dy] == grid[i][j]:
            perimeter -= 1
            if (i + dx, j + dy) not in visited:
                n_a, n_p = dfs1(i + dx, j + dy, visited, grid)
                area += n_a
                perimeter += n_p
    return area, perimeter


"""
Number of corners equals number of sides.

Two types of corners (inner and outer):

Inner (Where A is the block):

AA
AX

Outer (Where A is the block):
XX
XA
"""
def dfs2(i,j,visited, grid):
    visited.add((i,j))
    area, corners = 1,0
    for dy, dx in [(1,1),(1,-1),(-1,1),(-1,-1)]:
        neighbor_x = grid[i + dx][j] if 0 <= i + dx < len(grid) else None
        neighbor_y = grid[i][j + dy] if 0 <= j + dy < len(grid[0]) else None
        corner = grid[i + dx][j + dy] if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) else None
        if ((neighbor_x, neighbor_y) == (grid[i][j], grid[i][j]) and corner != grid[i][j]) or (grid[i][j] not in {neighbor_x, neighbor_y}):
            corners += 1
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and grid[i+dx][j+dy] == grid[i][j] and (i + dx, j + dy) not in visited:
            n_a, n_c = dfs2(i + dx, j + dy, visited, grid)
            area += n_a
            corners += n_c
    return area, corners

def part1():
    grid = input()
    visited = set()
    return sum(p * a for i in range(len(grid)) for j in range(len(grid[0])) if (i,j) not in visited for p,a in [dfs1(i,j,visited, grid)] )

def part2():
    grid = input()
    visited = set()
    return sum(p * a for i in range(len(grid)) for j in range(len(grid[0])) if (i,j) not in visited for p,a in [dfs2(i,j,visited, grid)] )
