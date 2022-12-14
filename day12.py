import sys, os
import itertools
from aoc import input, print, set_verbose
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

def render(m, filename='day12.png', scale=50, path=None, psize=20):
    rows, cols = len(m), len(m[0])
    image = np.zeros((rows, cols), dtype=np.uint8)
    dimage = np.zeros((rows, cols), dtype=np.uint8)
    for i,row in enumerate(m):
        for j,col in enumerate(row):
            image[i][j] = int(((col+2)*255/30.0))
            dimage[i][j] = int(((col)*255/30.0))

        im = Image.fromarray(np.uint8(image)).convert('L')
        dm = Image.fromarray(np.uint8(dimage)).convert('L')

    im = im.resize((cols*scale, rows*scale))

    mask = Image.new('L',(cols*scale, rows*scale) )
    im = im.filter(ImageFilter.GaussianBlur(radius=scale))
    if path:
        dm = dm.resize((cols*scale, rows*scale))
        draw = ImageDraw.Draw(mask)
        line = []
        for i,j in path:
            y = scale*i
            x = scale*j
            line.append((x,y))
        draw.line(line, (255,), width=psize)

    pathim = Image.composite(dm,im,mask)
    #dm.show()

    #im.show()
    #mask.show()
    pathim.show()
    pathim.save(filename, format='PNG')

def main():
    part1 = None
    part2 = None

    # Convert to numbers
    elevation = [list(map(lambda x : ord(x.replace('S','a').replace('E','z'))-97, line)) for line in input]
    
    # Record start/end positions
    # (starts is a list of all the coords with elevation of 'a')
    starts = set() 
    for i,row in enumerate(input):
        for j,col in enumerate(row):
            match col:
                case 'S':
                    start = (i,j)
                case 'E':
                    end = (i,j)
                case 'a':
                    starts.add((i,j))

    # Map dims
    rows = len(elevation)
    cols = len(elevation[0])
    
    # Return coords of all neighbors
    def neighbors(coord):
        i,j = coord
        return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]   

    # Set of all visitable squares (initially)
    Q = set(itertools.product(range(rows), range(cols)))
    
    # Distance from coordinate to the end square
    dist = {a : 10000000000000000000000000 for a in Q}
    prev = {a : None for a in Q}

    # By defintion, distance from end to end is zero
    dist[end] = 0

    # Djikstra
    while Q:
        u = sorted(Q, key=lambda coord : dist[coord])[0]
        Q.remove(u)
        for v in neighbors(u):
            if v not in Q:
                continue
            try:
                neighbor = elevation[v[0]][v[1]]
            except IndexError:
                continue 
            if elevation[u[0]][u[1]] - neighbor   > 1:
                continue

            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    S = []
    u = start
    if prev[u] is not None or u == end:
        while u != None:
            S = [u] + S
            u = prev[u]


    # dist[u] is now distance from u to 'E'
    part1 = dist[start]
    part2 = sorted([dist[i] for i in starts])[0]

    render(elevation, path=S)
    return (part1, part2)

if __name__ == '__main__':
    set_verbose(True)
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
