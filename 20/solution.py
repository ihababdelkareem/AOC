from collections import deque, defaultdict

def input():
    return list(map(list, open('input1.txt').read().splitlines()))

def bfs_from(start_x, start_y, grid):
    dist = {(start_x, start_y): 0}
    q = deque([(start_x, start_y)])
    while q:
        i, j = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and (i+dx,j+dy) not in dist:
                dist[(i+dx,j+dy)] = dist[(i,j)] + 1
                if grid[i+dx][j+dy] == '.':
                    q.append((i+dx,j+dy))
    return dist

def reachable_from_obstacle(start_x, start_y, grid, max_depth):
    dist = {(start_x,start_y): 0}
    q = deque([(start_x, start_y)])
    while q:
        i, j = q.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0 <= i + dx < len(grid) and 0 <= j + dy < len(grid[0]) and (i+dx,j+dy) not in dist and dist[(i,j)] < max_depth:
                q.append((i+dx,j+dy))
                dist[(i+dx,j+dy)] = dist[(i,j)] + 1
    res = set((x,y,dist) for (x,y),dist in dist.items() if grid[x][y] in 'SE.')
    return res


def count_with_max_cheat(cheat):
    grid = input()
    start_x, start_y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]
    end_x, end_y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'E'][0]
    dist_from_end = bfs_from(end_x, end_y, grid)
    dist_from_start = bfs_from(start_x, start_y, grid)
    total = dist_from_end[(start_x,start_y)]
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in 'S.':
                reachable = reachable_from_obstacle(i,j,grid,cheat)
                for reachable_x, reachable_y, depth in reachable:
                  if total - (depth + dist_from_start[(i,j)] + dist_from_end[(reachable_x, reachable_y)]) >= 100:
                      count += 1
    return count  

def part1():
    return count_with_max_cheat(2)

def part2():
    return count_with_max_cheat(20)