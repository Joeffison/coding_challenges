#!/usr/bin/env python3

import fileinput
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange

if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())
  for i in range(n_test_cases):
    x, y = map(int, f_in.readline().split())
    if x == y or (x > 1 and y == x - 2):
      if x % 2 == 0:
        print(x + y)
      else:
        print(x + y - 1)
    else:
      print('No Number')
