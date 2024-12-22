from collections import defaultdict

MOD = 16777216

def input():
    return list(map(int, open('input1.txt').read().splitlines()))

def transform(number):
    number = ((number << 6) ^ number) % MOD
    number = ((number >> 5) ^ number) % MOD
    number = ((number << 11) ^ number) % MOD
    return number

def part1():
    s = 0
    for number in input():
        for _ in range(2000):
            number = transform(number)
        s += number
    return s
        
def part2():
    s = 0
    diff_count = defaultdict(int)
    for number in input():
        current_diff = []
        diffs_seen_for_number = set()
        for _ in range(2000):
            prev = number
            number = transform(number)
            current_diff.append(number % 10 - prev % 10)
            if len(current_diff) >= 4 and tuple(current_diff[-4:]) not in diffs_seen_for_number:
                diff = tuple(current_diff[-4:])
                diffs_seen_for_number.add(diff)
                diff_count[diff] += number % 10
    return max(diff_count.values())