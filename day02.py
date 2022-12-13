import sys, os
import itertools
import input
SCORES = {
        'AX' : 3,
        'BX' : 0,
        'CX' : 6,
        'AY' : 6,
        'BY' : 3,
        'CY' : 0,
        'AZ' : 0,
        'BZ' : 6,
        'CZ' : 3,
    }
# ABC,XYZ = Rock paper scissors
def score(abc,xyz):
    myscore = SCORES[abc+xyz]
    opponentscore = 6-myscore
    opponentshape = 'ABC'.index(abc)+1 
    myshape = 'XYZ'.index(xyz)+1
    return (myscore + myshape, opponentscore + opponentshape)

def pickshape(abc,outcome):
    for key, value in SCORES.items():
        if key.startswith(abc):
            if outcome == 'X' and value == 0:
                return key[1]
            elif outcome == 'Y' and value == 3:
                return key[1]
            elif outcome == 'Z' and value == 6:
                return key[1]

def main():
    part1 = 0
    part2 = 0

    for line in input:
        abc, xyz = line.strip().split()
        part1 += score(abc, xyz)[0]
        part2 += score(abc, pickshape(abc, xyz))[0]

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
