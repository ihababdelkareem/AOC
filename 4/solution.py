def input():
    return [l.rstrip('\n') for l in open('input1.txt').readlines()]

def sub(i,j,dx,dy,lines,m,n,search):
    sub = ""
    while 0 <= i < m and 0 <= j < n and len(sub) != len(search):
        sub += lines[i][j]
        i, j = i + dx, j + dy
    return sub == search
    
def part1(): # Check every coordinate
    lines = input()
    m,n = len(lines), len(lines[0])
    delta = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]
    return sum(sub(i,j,*d,lines,m,n,'XMAS') for i in range(m) for j in range(n) for d in delta)

def part2(): # Check blocks of 3*3
    lines = input()
    m,n = len(lines), len(lines[0])
    return sum(sum(sub(x,y,dx,dy,lines,m,n,'MAS') for x, y, dx, dy in [(i,j,1,1), (i+2,j,-1,1), (i,j+2,1,-1), (i+2,j+2,-1,-1)]) == 2 for i in range(m) for j in range(n))
