import sys, os
import itertools
import input

def overlap(a,b,c,d):
    ab = range(a,b+1)
    cd = range(c,d+1)
    print(ab)
    print(cd)
    ovl = set.intersection(set(ab),set(cd))
    if ovl:
        return (min(ovl),max(ovl))
    else:
        return None

def main():
    part1 = 0
    part2 = 0

    for line in input:
        ab,cd = line.strip().split(',')
        a,b = tuple(map(int, ab.split('-')))
        c,d = tuple(map(int, cd.split('-')))
        ovl = overlap(a,b,c,d)

        if (a,b) == ovl or (c,d) == ovl:
            part1 += 1
        if ovl:
            part2 += 1

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
