INF = float('inf')
import re

def input():
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)"
    parsed_data = []
    with open("input1.txt", 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        for match in matches:
            a_x, a_y, b_x, b_y, t_x, t_y = map(int, match)
            parsed_data.append((a_x, b_x, t_x, a_y, b_y, t_y))
    return parsed_data

"""
a*a_x + b*b_x = t_x
a*a_y + b*b_y = t_y
"""
def solve(a_x, b_x, t_x, a_y, b_y, t_y):
  det = a_x * b_y - a_y * b_x
  if det == 0:
    return 0
  a = (t_x * b_y - t_y * b_x) / det
  b = (a_x * t_y - a_y * t_x) / det
  return (3 * int(a) + int(b)) if (a,b) == (int(a), int(b)) else 0

def part1_and_2():
    return sum(solve(*input_) for input_ in input())