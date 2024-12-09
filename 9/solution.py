from collections import defaultdict
def input():
    return open('input1.txt').read()

def part1():
    line = input()
    disk = []
    for i in range(0, len(line), 2):
         occupied, available = int(line[i]), (int(line[i+1]) if i + 1 < len(line) else 0)
         disk.append([available, occupied * [i//2]])
    left, right = 0, len(disk) - 1
    while left < right:
         if disk[left][0] == 0:
              left += 1
         elif len(disk[right][1]) == 0:
              right -= 1
         else:
              disk[left][1].append(disk[right][1].pop())
              disk[left][0] -= 1
              disk[right][0] += 1
    i, res = 0, 0
    for _, block in disk:
         for id in block:
              res += i * id
              i += 1    
    return res
          
def part2():
    line = input()
    disk = []
    for i in range(0, len(line), 2):
         occupied, available = int(line[i]), (int(line[i+1]) if i + 1 < len(line) else 0)
         disk.append([0, occupied * [i//2], [], available])
    for cand_idx in reversed(range(len(disk))):
        for dest_idx in range(cand_idx):
            if len(disk[cand_idx][1]) <= disk[dest_idx][3]:
                while disk[cand_idx][1]:
                    disk[dest_idx][2].append(disk[cand_idx][1].pop())
                    disk[dest_idx][3] -= 1
                    disk[cand_idx][0] += 1                
                break
    i, res = 0, 0
    for remaining_left, original_block, filled_block, remaining_right in disk:
        for _ in range(remaining_left):
             i += 1
        for id in original_block:
             res += i * id
             i += 1    
        for id in filled_block:
             res += i * id
             i += 1
        for _ in range(remaining_right):
             i += 1
    return res