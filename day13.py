import sys, os
import itertools
import input
from functools import cmp_to_key

def main():
    part1 = None
    part2 = None

    packet_pairs = input.all.split('\n\n')

    def compare(left,right):

        if isinstance(left, int) and isinstance(right, int):
            return None if left == right else left < right

        elif isinstance(left, list) and isinstance(right, list):
            i=0
            while True:
                try:
                    l = left[i]
                except IndexError:
                    if len(left) < len(right):
                        return True
                    else:
                        return None
                try:
                    r = right[i]
                except IndexError:
                    return False
                v = compare(l,r)            
                if v is not None:
                    return v
                i+=1

        if isinstance(left, int) and isinstance(right, list):
            return compare([left],right)
        if isinstance(left, list) and isinstance(right, int):
            return compare(left,[right])
        print('none')
        return None
    part1 = []
    all_packets = []
    for i, pair in enumerate(packet_pairs):
        p1,p2 = tuple(map(eval,pair.split()))
        all_packets.extend([p1,p2])
        if compare(p1,p2):
            part1.append(i+1)
    
    part1 = sum(part1)
    all_packets.extend([[[2]],[[6]]])
    
    def cmp(left, right):
        return -1 if compare(left, right) else 1

    all_packets = sorted(all_packets, key=cmp_to_key(cmp))
    for item in all_packets:
        print(item)

    part2 = (all_packets.index([[2]])+1)*(all_packets.index([[6]])+1)

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
