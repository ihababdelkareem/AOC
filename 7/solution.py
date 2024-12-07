def input():
    return [[int(line[0])] + list(map(lambda term: int(term), line[1].strip().split(' '))) for line in list(map(lambda line: line.rstrip('\n').split(':'), open('input1.txt').readlines()))]

def eval(nums, ops):
    op_map = {'+': lambda x,y: x + y, '*': lambda x,y: x * y, 'C': lambda x,y: int(str(x) + str(y))}
    while len(nums) != 1:
        nums[0] = op_map[ops[0]](nums[0], nums[1])
        nums.pop(1)
        ops.pop(0)
    return nums[0]

def generate_operations(size, concat = False):
    def backtrack():
        if len(buffer) == size:
            perms.append(buffer[::])
        else:
            for op in ops:
                buffer.append(op)
                backtrack()
                buffer.pop()
    ops = ['+', '*'] + (['C'] if concat else [])
    buffer = []
    perms = []
    backtrack()
    return perms
            
def part1():
    ops_cache = [generate_operations(i) for i in range(15)]
    return sum(line[0] for line in input() if any(eval(line[1:], ops_cache[len(line) - 2][i][::]) == line[0] for i in range(len(ops_cache[len(line) - 2]))))
    
def part2():
    ops_cache = [generate_operations(i, True) for i in range(15)]
    return sum(line[0] for line in input() if any(eval(line[1:], ops_cache[len(line) - 2][i][::]) == line[0] for i in range(len(ops_cache[len(line) - 2]))))