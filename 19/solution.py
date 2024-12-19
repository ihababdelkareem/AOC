def input():
    tokens, words = [], set()
    split = False
    lines = open('input1.txt').read().splitlines()
    for line in lines:
        if line == '':
            split = True
        elif not split:
            tokens = line.split(', ')
        else:
            words.add(line)
    return tokens, words

def dfs(start, word, tokens, mem):
    if start == len(word):
        return 1
    if start not in mem:
        mem[start] = sum(dfs(end + 1, word, tokens, mem) for end in range(start, len(word)) if word[start:end+1] in tokens)
    return mem[start]

def part1():
    tokens, words = input()
    return sum(dfs(0,word,tokens,dict()) > 0 for word in words)

def part2():
    tokens, words = input()
    return sum(dfs(0,word,tokens,dict()) for word in words)