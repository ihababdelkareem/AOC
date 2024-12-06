def input():
    return list(map(lambda line: list(line.rstrip('\n')), open('input1.txt').readlines()))

def finish_or_cycle(grid, row, col):
    m,n,diff = len(grid), len(grid[0]), [(-1,0),(0,1),(1,0),(0,-1)] # U, R, D, L
    dir, visited_cells, visited_obstacles = 0, set(), set()
    while 0 <= row < m and 0 <= col < n:
        visited_cells.add((row, col))
        dx, dy = diff[dir]
        if 0 <= row + dx < m and 0 <= col + dy < n and grid[row + dx][col + dy] == '#':
            if (dir, row + dx, col + dy) in visited_obstacles:
                return True, set()
            else:
                visited_obstacles.add((dir, row + dx, col + dy))
                dir = (dir + 1) % 4
                dx, dy = diff[dir]
        else:
            row, col = row + dx, col + dy
    return False, len(visited_cells)
    
def part1():
    grid = input()
    start_1D = ''.join(list(map(lambda line: ''.join(line), grid))).find('^')
    row, col = start_1D // len(grid), start_1D % len(grid)
    return finish_or_cycle(grid, row, col)[1]

def part2():
    grid = input()
    start_1D = ''.join(list(map(lambda line: ''.join(line), grid))).find('^')
    row, col = start_1D // len(grid), start_1D % len(grid)
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                count += finish_or_cycle(grid, row, col)[0]
                grid[i][j] = '.'
    return count