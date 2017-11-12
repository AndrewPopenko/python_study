import string
import sys


step = int(sys.argv[1])

for i in range(step, 0, -1):
    string = ''
    for j in range(0, step+1):
        if j == i or j > i:
            string += '*'
        else:
            string += ' '
    print(string)
