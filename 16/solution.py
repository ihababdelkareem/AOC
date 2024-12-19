from heapq import heappush, heappop
from collections import defaultdict

INF = float('inf')
def input():
    return open('input1.txt').read().splitlines()

def traverse_parent_tree(x, y, dx, dy, parent_tree, visited, res, grid):
    if grid[x][y] == 'S':
        res.append(visited[::])
    else:
        visited.append((x, y, dx, dy))
        for cx, cy, cdx, cdy in parent_tree[(x,y,dx,dy)]:
            traverse_parent_tree(cx, cy, cdx, cdy, parent_tree, visited, res, grid)
        visited.pop()

def part1():
    grid = input()
    start_x, start_y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]
    queue = [(0, 0, 1, start_x, start_y)]
    dist = defaultdict(lambda: INF)
    while queue:
        cost, dx, dy, x, y = heappop(queue)
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == '#' or cost > dist[(x,y)]:
            continue
        dist[(x,y)] = cost
        if grid[x][y] == 'E':
            return cost
        for new_dx, new_dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            heappush(queue, (cost + 1 + max(abs(new_dx - dx), abs(new_dy - dy)) * 1000, new_dx, new_dy, x + new_dx, y + new_dy))
    return -1

def part2():
    grid = input()
    start_x, start_y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'S'][0]
    queue = [(0, 0, 1, start_x, start_y, 0, 0)]
    parent_tree = defaultdict(set)
    dist = defaultdict(lambda: INF)
    while queue:
        cost, dx, dy, x, y, pdx, pdy = heappop(queue)
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] == '#' or cost > dist[(dx,dy,x,y)]:
            continue
        dist[(dx,dy,x,y)] = cost
        px, py = x - dx, y - dy
        parent_tree[(x,y,dx,dy)].add((px,py,pdx,pdy))
        if grid[x][y] != 'E':
            for new_dx, new_dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                heappush(queue, (cost + 1 + max(abs(new_dx - dx), abs(new_dy - dy)) * 1000, new_dx, new_dy, x + new_dx, y + new_dy, dx, dy))
    res = []
    end_x, end_y = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'E'][0]
    best_path = min(dist[(0,1,end_x,end_y)], dist[(0,-1,end_x,end_y)], dist[(1,0,end_x,end_y)], dist[(-1,0,end_x,end_y)])
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        if dist[(dx,dy,end_x,end_y)] == best_path:
            traverse_parent_tree(end_x,end_y,dx,dy,parent_tree,[],res,grid)
    return 1 + len(set((x,y) for path in res for x,y,_,_ in path))
