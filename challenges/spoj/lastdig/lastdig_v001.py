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
    a, b = map(int, f_in.readline().split())
    p = a % 10
    q = b % 4

    if a == 0 or a % 10 == 0:
      print(0)
    elif b == 0:
      print(1)
    elif q == 0:
      print((p**4) % 10)
    else:
      print((p**q) % 10)
