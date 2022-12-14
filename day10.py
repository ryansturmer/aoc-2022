import sys, os
import itertools
import input

def main():
    part1 = 0
    part2 = None
    cycle = 0
    current_cycles = 0
    x = 1
    instructions = list(input)
    instr = None
    instruction_set = {
        'noop' : 1,
        'addx' : 2
    }
    part1_cycles = [20,60,100,140,180,220]
    screen = ['.']*240

    while True:        
        if not instr:
            try:
                instr = instructions.pop(0).split()
                print(instr)
            except:
                break
            current_cycles = instruction_set[instr[0]]            
        if cycle%40 in (x-1, x, x+1):
            screen[cycle] = '#'

        cycle += 1
        current_cycles -= 1
        print(cycle,x)

        if cycle in part1_cycles:
            print(cycle, x*cycle)
            part1 += x*cycle
        

        if current_cycles == 0:
            match instr[0]:
                case 'addx':
                    x += int(instr[1])
                case 'noop':
                    pass
            instr = None


    part2 = '\n'.join([''.join(screen[x:x+40]) for x in range(0, 201, 40)])
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
