from copy import copy
from ctypes import c_int
import cmath

ORIGINAL_BIFS = copy(__builtins__.__dict__)
BANNED = ['global',
          'local',
          '__',
          'eval',
          'exec',
          'pickle',
          '+',
          '-',
          '[',
          ']',
          'reduce',
          'os',
          'subprocess',
          'import',
          'input',
          'ban',
          'sys']

def challenge(x, y):
    if x >= 0 and y >= 0:
        x = c_int(x)
        y = c_int(y)

        if cmath.phase(complex(x.value ,y.value)) == cmath.pi:
            print "FLAG-XXXXXXXXXXXXXXXXXXXXXX"

def main():

    def jail():
        process()

    def process():
        text = raw_input()
        for ban in BANNED:
            if text.find(ban) != -1:
                return True
        run(text)
        return True

    def run(text):
        namespace = {}
        namespace['challenge'] = challenge

        exec text in namespace

    def strip_bifs():
        target = __builtins__.__dict__.keys()
        target.remove('raw_input')
        for x in target:
            del __builtins__.__dict__[x]

    while True:
        jail()


if __name__ == '__main__':
    main()
