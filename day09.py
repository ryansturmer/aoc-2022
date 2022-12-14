import sys, os
import itertools
import input
import numpy as np
from PIL import Image 
# . . . . . . .
# . . T T T . .       (2,1)(2,0)(2,-1)
# . T . . . T .  (1,2)                (1,-2)
# . T . H . T .  (0,2)                (0,-2)
# . T . . . T .  (-1,2)               (-1,-2)
# . . T T T . .      (-2,1)(-2,0)(-2,-1)
# . . . . . . .

def render(ropes, skip_frames=20, decay_rate=1, filename='day09.gif'):
    print("Rendering %d frames" %  (len(ropes)//skip_frames))
    frames = []
    images = []
    minrow,maxrow = 0,0
    mincol,maxcol = 0,0
    for rope in ropes:
        maxrow = max(maxrow, max([k[0] for k in rope]))
        maxcol = max(maxcol, max([k[1] for k in rope]))
        minrow = min(minrow, min([k[0] for k in rope]))
        mincol = min(mincol, min([k[1] for k in rope]))

    rows = maxrow-minrow + 1
    cols = maxcol-mincol + 1
    #ropes = [[(k[0]-minrow, k[1]-mincol) for k in rope] for rope in ropes ]
    visited = set() 
    age = {}
    
    for fc,rope in enumerate(ropes):
        image = np.zeros((rows, cols), dtype=int)
        for r,c in visited:
            image[r][c] = age[(r,c)]
        for row,col in rope:
            row,col = row-minrow, col-mincol
            visited.add((row,col))
            age[(row,col)] = 255
            image[row][col] = 255
        im = Image.fromarray(np.uint8(image)).convert('RGB')
        if fc % skip_frames == 0:
            frames.append(im)
        for key in age:
            age[key] = max(age[key]-decay_rate, 0)
    frames[0].save(filename, format='GIF', append_images=frames[1:], save_all=True, duration=0, loop=0)


def move(pos, dir):
    return {'L':(pos[0],pos[1]-1),'R':(pos[0],pos[1]+1),'U':(pos[0]-1, pos[1]),'D':(pos[0]+1,pos[1])}[dir]

def diff(a,b):
    return (a[0]-b[0], a[1]-b[1])

def simulate(rope):
    visited = set()
    ropes = []
    for line in input:
        dir, count = line.split()[0], int(line.split()[1])
        while count > 0:
            rope[0] = move(rope[0], dir)            
            for i in range(1,len(rope)):
                delta = diff(rope[i-1], rope[i])
                dlink = {
                    (2,1)   : 'RD',
                    (2,0)   : 'D',
                    (2,-1)  : 'LD',
                    (1,-2)  : 'LD',
                    (0,-2)  : 'L',
                    (-1,-2) : 'LU',
                    (-2,-1) : 'LU',
                    (-2,0)  : 'U',
                    (-2,1)  : 'RU',
                    (-1,2)  : 'RU',
                    (0,2)   : 'R',
                    (1,2)   : 'RD',
                    # Possible in part 2 but not part 1
                    (2,2)   : 'RD',
                    (2,-2)  : 'LD',
                    (-2,2)  : 'RU',
                    (-2,-2) : 'LU'
                }.get(delta, '')
            
                for c in dlink:
                    rope[i] = move(rope[i], c)
            
            visited.add(rope[-1])
            count -= 1
            ropes.append(rope[:])

    return ropes, len(visited)

def main():
    part1 = None
    part2 = None
    
    part1ropes, part1 = simulate([(0,0)]*2)
    part2ropes, part2 = simulate([(0,0)]*10)

    render(part2ropes, filename='day09-part1.gif')
    render(part2ropes  filename='day09-part2.gif')
        
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
