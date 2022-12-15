import sys, os
import itertools
from aoc import input, print, set_verbose

def main():
    part1 = None
    part2 = None
    sensors = {}
    beacons = {}

    def dist(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    beacons = set()
    all_points = set()
    dists = []
    sd = {}
    for line in input:
        parts = line.split()
        sx = int(parts[2].split('=')[-1].strip(','))
        sy = int(parts[3].split('=')[-1].strip(':'))
        bx = int(parts[-2].split('=')[-1].strip(','))
        by = int(parts[-1].split('=')[-1])
        sd[(sx,sy)] = dist((sx,sy), (bx,by))
        sensors[(sx,sy)] = (bx,by)
        beacons.add((bx,by)) 
        all_points.add((sx,sy))
        all_points.add((bx,by))
        dists.append(dist((sx,sy), (bx,by)))

    minx, miny = min([p[0] for p in all_points]), min([p[1] for p in all_points])
    maxx, maxy = max([p[0] for p in all_points]), max([p[1] for p in all_points])

    a = (minx-max(dists), miny-max(dists))
    b = (maxx+max(dists), maxy+max(dists))


    def can_position_have_beacon(p):
        if p in beacons:
            return True

        for sensor, beacon in sensors.items():
            if dist(sensor, p) <= sd[sensor]:
                return False
        
        return True

    part1 = 0
    for x in range(a[0], b[0]):
        part1 += 1 if not can_position_have_beacon((x,2000000)) else 0

    #for a in sensors.keys():
    #    sensors[a] = min([(b, dist(a,b)) for b in beacons.keys()], key=lambda x : x[1])

    print(sensors)
    print(beacons)
    return (part1, part2)

if __name__ == '__main__':
    part1, part2 = main()
    set_verbose(True)
    print('------------------------')
    print('  🎄 Advent of Code 🎄')
    print('------------------------')
    print('')
    print('Part 1 Solution: ⭐️')
    print(part1)

    print('\n')
    print('Part 2 Solution: ⭐️⭐️')
    print(part2)
    print('')
