import sys, os
import itertools
import input
from math import prod

def pretty(g):
    return '\n'.join([''.join(map(str, row)) for row in g])
def main():
    part1 = None
    part2 = None

    rows = [list(map(int, line)) for line in input]
    cols = list(zip(*rows))
    visible = [[0]*len(row) for row in rows]
    scenic_score = [[0]*len(row) for row in rows]

    def viewing_distance(tree, trees):
        s = 0
        for t in trees:
            s+=1
            if t >= tree:
                break
        return s

    for i in range(len(rows)):
        for j in range(len(cols)):
            tree = rows[i][j]
            a = list(reversed(rows[i][:j]))
            b = rows[i][j+1:]
            c = list(reversed(cols[j][:i]))
            d = cols[j][i+1:]
            if any([max(x, default=-1) < tree for x in (a,b,c,d)]):
                visible[i][j] = 1
            
            scenic_score[i][j] = prod([viewing_distance(tree, x) for x in (a,b,c,d)])
            print([viewing_distance(tree, x) for x in (a,b,c,d)])
    part1 = sum([sum(row) for row in visible])
    part2 = max([max(row) for row in scenic_score])

    print(pretty(scenic_score))

    return (part1, part2)

if __name__ == '__main__':
    part1, part2 = main()
    print('-----------------------')
    print('    Advent of Code')
    print('-----------------------')
    print('')
    print('Part 1 Solution:')
    print(part1)

    print('\n')
    print('Part 2 Solution:')
    print(part2)
    print('')
