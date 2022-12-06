import sys, os
import itertools
import input

def main():
    part1 = None
    part2 = None

    initial_state, instructions = '\n'.join(list(input)).split('\n\n')
    transposed = [''.join(line) for line in itertools.zip_longest(*initial_state.split('\n'), fillvalue=' ')]
    stacks = {}
    for line in transposed:
        if line[-1] in '0123456789':
            stacks[int(line.strip()[-1])] = list(reversed(line.strip()[:-1]))
    instructions = [tuple(int(x.split()[y]) for y in [1,3,5]) for x in instructions.split('\n')]
    
    stacks2 = {k:v[:] for k,v in stacks.items()}

    for count, source, dest in instructions:
        crates = stacks2[source][-count:]
        stacks2[source] = stacks2[source][:-count]
        stacks2[dest].extend(crates)

        while count > 0:
            stacks[dest].append(stacks[source].pop())
            count-=1


    part1 = ''.join([stacks[key][-1] for key in sorted(stacks.keys())])
    part2 = ''.join([stacks2[key][-1] for key in sorted(stacks2.keys())])

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
