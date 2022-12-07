import sys, os
import itertools
import input

def main():
    part1 = None
    part2 = None
    root = {'parent': None, 'children' : {}}
    current_dir = root
    index = [root]
    for line in input:
        parts = line.split()
        if parts:
            if parts[0] == '$':
                if parts[1] == 'cd':
                    dir = parts[2]
                    if dir == '..':
                        current_dir = current_dir['parent']
                    elif dir == '/':
                        current_dir = root
                    else:
                        name = parts[2]
                        if name not in current_dir['children']:
                            # Inference case: Infer that a directory exists because we went there
                            # current_dir['children'][name] = {'name' : name, 'parent':current_dir, 'children' : {}}
                            pass
                        current_dir = current_dir['children'][name]
                elif parts[1] == 'ls':
                    pass
            else:
                name = parts[1]
                if parts[0] == 'dir':
                    current_dir['children'][name] = { 'name' : name, 'parent':current_dir, 'children' : {}}
                    index.append(current_dir['children'][name])
                else:
                    size = int(parts[0])
                    current_dir['children'][name] = size

    def compute_sizes(d):
        size = 0
        for name, child in d['children'].items():
            if isinstance(child, int):
                size += child
            else:
                size += compute_sizes(child)
        # Make size annotation
        d['size'] = size
        return size
    
    compute_sizes(root)

    # PART 1
    part1 = 0
    for d in index:
        if d['size'] <= 100000:
            part1 += d['size']

    # PART 2
    FILESYSTEM_SIZE = 70000000
    UPDATE_SIZE = 30000000
    used_size = root['size']
    free_size = FILESYSTEM_SIZE-used_size
    need_size = UPDATE_SIZE-free_size
    dirs_large_enough = sorted(filter(lambda d : d['size'] >= need_size, index), key=lambda d : d['size'])
    part2 = dirs_large_enough[0]['size']
    
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
