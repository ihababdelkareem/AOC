from collections import defaultdict
def input_():
    graph = defaultdict(set)
    for line in open('input1.txt').read().splitlines():
        a,b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def is_connected(nodes, graph):
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if not (nodes[i] in graph[nodes[j]] and nodes[j] in graph[nodes[i]]):
                return False
    return True

def groups_of_three(graph):
    keys = list(graph.keys())
    groups = set()
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            for k in range(j + 1, len(keys)):
                first, second, third = keys[i], keys[j], keys[k]
                connected = is_connected((first, second, third), graph)
                if connected:
                    groups.add(tuple(sorted((first,second,third))))
    return groups       

def part1():
    graph = input_()
    return sum('t' in a[0]+b[0]+c[0] for a,b,c in groups_of_three(graph))

def part2():
    graph = input_()
    groups = groups_of_three(graph)
    merged_groups = set()
    while True:
        merged_groups = set()
        merge = False
        for group in groups:
            for new_node in graph.keys():
                if new_node not in group and is_connected(group + (new_node,),graph):
                    merged_groups.add(tuple(sorted(group + (new_node,))))
                    merge = True
        if not merge:
            break
        groups = merged_groups
    return ','.join(groups.pop())