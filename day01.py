import sys
def main(input):
    with open(input) as fp:
        lines = fp.readlines()
    elves = [0]
    for line in lines:
        if not line.strip():
            elves.append(0)
        else:
            elves[-1]+=int(line)
    return list(reversed(sorted(elves)))

if __name__ == '__main__':
    elves = main(sys.argv[1] or 'input.txt')
    print("Part 1: ", elves[0])
    print("Part 2: ", sum(elves[:3]))
