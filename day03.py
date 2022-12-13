import sys, os
import itertools
import input

def priority(item):
    return ord(item)-96 if item.islower() else ord(item)-38

def main():
    part1 = None
    part2 = None
    common_types = []
    for sack in input:
        a = sack[:len(sack)//2]
        b = sack[len(sack)//2:]
        common = set(a).intersection(set(b))
        common_types.append(list(common)[0])
    part1 = sum(priority(item) for item in common_types)

    part2 = 0
    items = list(input)
    for i in range(0, len(items), 3):
        a,b,c = map(set, items[i:i+3])
        part2 += priority(list(set.intersection(a,b,c))[0])

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
