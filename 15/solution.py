LOOKUP = {'^':(-1,0),'v':(1,0),'>':(0,1),'<':(0,-1)}

def input_():
    lines = open('input1.txt').read().splitlines()
    split = False
    instructions = ''
    grid = []
    for line in lines:
        if line == '':
            split = True
        elif not split:
            grid.append(list(line))
        else:
            instructions += line
    return grid, instructions

def apply_part1(i,j,grid,instruction):
    dx, dy = LOOKUP[instruction]
    x,y = i + dx, j + dy
    while grid[x][y] == 'O':
        x += dx
        y += dy
    if grid[x][y] == '.':
        while grid[x - dx][y - dy] != '@':
            grid[x][y], grid[x - dx][y - dy] = grid[x - dx][y - dy], grid[x][y]
            x,y = x - dx, y - dy
        grid[x][y], grid[x - dx][y - dy] = grid[x - dx][y - dy], grid[x][y]
        return x,y
    else:
        return i, j

def apply_part2(robot_i,robot_j,grid,instruction):
    other_bracket_diff = {'[':1,']':-1}
    def can_complete_move(x,y,depth):
        if grid[x][y] == '.':
            return True
        if grid[x][y] == '#':
            return False
        cells_to_move.append((depth,x,y))
        if dy != 0:
            return can_complete_move(x, y + dy, depth + 1)
        else:
            up =  can_complete_move(x + dx, y,depth + 1) if (depth + 1, x + dx, y) not in cells_to_move else True
            same = can_complete_move(x, y + other_bracket_diff[grid[x][y]], depth) if (depth, x, y + other_bracket_diff[grid[x][y]]) not in cells_to_move else True
            return up and same
    dx, dy = LOOKUP[instruction]
    cells_to_move= [(-1,robot_i, robot_j)]
    if (can_complete_move(robot_i + dx, robot_j + dy, 0)):
        for _,x,y in reversed(sorted(cells_to_move)):
            grid[x + dx][y + dy] = grid[x][y]
            grid[x][y] = '.'
        return robot_i + dx, robot_j + dy
    return robot_i, robot_j

def transform_grid(grid):
    mapper = {'#':'##','O':'[]','.':'..','@':'@.'}
    new_grid = []
    for row in grid:
        new_grid.append(list(''.join(list(map(lambda cell: mapper[cell], row)))))
    return new_grid

def part1():
    grid, instructions = input_()
    x, y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '@'][0]
    for instruction in instructions:
        x, y = apply_part1(x,y,grid,instruction)
    return sum(i * 100 + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'O')

def part2():
    grid, instructions = input_()
    grid = transform_grid(grid)
    x, y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '@'][0]
    for instruction in instructions:
        x, y = apply_part2(x,y,grid,instruction)
    return sum(i * 100 + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '[')