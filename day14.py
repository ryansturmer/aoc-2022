import sys, os
import itertools
og_input = input
import input

def main():
    part1 = None
    part2 = None
    
    rocks = []
    sand = []
    for path in input:
        rocks.append([])
        points = path.split('->')
        for point in points:
            x,y = tuple(map(int, point.split(',')))
            rocks[-1].append((x,y))

    def line(a,b):
        x1,y1 = a
        x2,y2 = b
        return set(itertools.product(range(min(x1,x2), max(x1,x2)+1), range(min(y1,y2),max(y1,y2)+1)))

    all_rocks = set()
    for path in rocks:
        for i in range(len(path)-1):
            a,b = path[i], path[i+1]
            rock_points = line(a,b)
            all_rocks = set.union(all_rocks,rock_points)
    
    current_sand = (500,0)
    all_sand = set()
    sand_count = 0
    floor = 2+max([p[1] for p in all_rocks])
    while True:
        tx,ty = current_sand
        ty+=1
        if (tx,ty) in all_rocks or (tx,ty) in all_sand:
            tx-=1
        if (tx,ty) in all_rocks or (tx,ty) in all_sand:
            tx+=2
        if ty == floor or ((tx,ty) in all_rocks or (tx,ty) in all_sand):
            all_sand.add(current_sand)
            sand_count += 1
            print(sand_count)
            if current_sand == (500,0):
                break
            current_sand = (500,0)
            #og_input()
            continue
    
        current_sand = tx,ty
        #print(current_sand)

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
