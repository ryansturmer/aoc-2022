import sys
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
sys.modules[__name__] = AOCInput()
