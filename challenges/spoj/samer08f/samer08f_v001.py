#!/usr/bin/env python3

import fileinput
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange

if __name__ == '__main__':
  dp_feynman = [1, 5]
  for n in fileinput.input():
    n = int(n) - 1
    if n < 0:
      break

    for i in range(len(dp_feynman) - 1, n):
      dp_feynman.append((i + 2)**2 + dp_feynman[i])
    print(dp_feynman[n])
