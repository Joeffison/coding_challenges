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
    n_participants = int(f_in.readline())
    group1 = sorted(map(int, f_in.readline().split()))
    group2 = sorted(map(int, f_in.readline().split()))
    print(sum([group1[j] * group2[j] for j in range(n_participants)]))
