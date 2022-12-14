import sys
_og_print = print

class AOCInput(object):
    def __iter__(self):
        try:
            filename = sys.argv[1]
        except:
            filename = 'input.txt'
        with open(filename) as fp:
            return iter([line.rstrip('\n') for line in fp.readlines()])
    @property
    def all(self):
        try:
            filename = sys.argv[1]
        except:
            filename = 'input.txt'
        with open(filename) as fp:
            return fp.read()

_aoc_verbose = True

def aoc_print(*args, **kwargs):
    global _aoc_verbose
    if _aoc_verbose:
        _og_print(*args, **kwargs)

def set_verbose(value):
    global _aoc_verbose
    _aoc_verbose = bool(value)

input = AOCInput()
print = aoc_print
