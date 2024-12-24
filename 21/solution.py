from collections import defaultdict
KEYPAD = {'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1),'3':(2,2),'': (3,0),'0':(3,1),'A':(3,2)}
ARROWS = {'': (0,0), '^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2)}
PATH_CACHE = defaultdict(lambda: defaultdict(list))
DFS_CACHE = dict()
def input():
    return open('input1.txt').read().splitlines()
def build_path_cache(map):
    for key in map:
        for other_key in map:
            PATH_CACHE[key][other_key] = generate_paths(key,other_key,map)
 
def generate_paths(key_from, key_to, map):
    def backtrack(current,target,buffer):
        if current == target:
            res.append(buffer)
        else:
            current_x, current_y = current
            target_x, target_y = target
            avoid_x, avoid_y = map['']
            if current_x > target_x:
                suffix = ''
                while current_x > target_x and (current_x - 1, current_y) != (avoid_x, avoid_y):
                    suffix += '^'
                    current_x -= 1
                if suffix:
                    backtrack((current_x,current_y),target,buffer + suffix)
            elif current_x < target_x:
                suffix = ''
                while current_x < target_x and (current_x + 1, current_y) != (avoid_x, avoid_y):
                    suffix += 'v'
                    current_x += 1
                if suffix:
                    backtrack((current_x,current_y),target,buffer + suffix)
            current_x, current_y = current
            if current_y > target_y:
                suffix = ''
                while current_y > target_y and (current_x, current_y - 1) != (avoid_x, avoid_y):
                    suffix += '<'
                    current_y -= 1
                if suffix:
                    backtrack((current_x,current_y),target,buffer + suffix)
            elif current_y < target_y:
                suffix = ''
                while current_y < target_y and (current_x, current_y + 1) != (avoid_x, avoid_y):
                    suffix += '>'
                    current_y += 1
                if suffix:
                    backtrack((current_x,current_y),target,buffer + suffix)
    res = []
    backtrack(map[key_from],map[key_to],'')
    return res
def dfs(from_, to_, depth, target_depth, cache):
    if depth == target_depth:
        return 1
    if (from_, to_, depth) in cache:
        return cache[(from_, to_, depth)]
    paths_between_arrows = PATH_CACHE[from_][to_]
    res = float('inf')
    for path_between_arrows in paths_between_arrows:
        path_between_arrows = 'A' + path_between_arrows + 'A'
        res = min(res, sum(dfs(path_between_arrows[i-1],path_between_arrows[i],depth + 1, target_depth, cache) for i in range(1, len(path_between_arrows))))
    cache[(from_, to_, depth)] = res
    return res
build_path_cache(KEYPAD)
build_path_cache(ARROWS)
def part1():
    return sum(int(code[:-1]) * sum(dfs('A' if i == 0 else code[i-1],code[i],0,3,DFS_CACHE)for i in range(len(code))) for code in input())
def part2():
    return sum(int(code[:-1]) * sum(dfs('A' if i == 0 else code[i-1],code[i],0,26,DFS_CACHE)for i in range(len(code))) for code in input())
