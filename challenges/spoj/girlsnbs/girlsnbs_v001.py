#!/usr/bin/env python3

import fileinput
import math
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange

if __name__ == '__main__':
  for line in fileinput.input():
    g1, g2 = sorted(map(float, line.split()))
    if g1 == -1:
      break
    elif g1 == 0 and g2 == 0:
      print(0)
    elif g1 > g2:
      print(int(math.ceil(g1 / (g2 + 1))))
    else:
      print(int(math.ceil(g2 / (g1 + 1))))
