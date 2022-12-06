import sys, os
import itertools
import input

def find_start(msg, size):
    for i in range(size, len(msg)):
        if len(set(msg[i-size:i])) == size:
            return msg[i-size:i], i
    return None, None

def main():
    part1 = None
    part2 = None
    msg = list(input)[0].strip()
    part1 = find_start(msg, 4)
    part2 = find_start(msg, 14)

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
