#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    # there is an empty line before each test case
    f_in.readline()

    n = int(f_in.readline())
    remainder = 0
    for j in range(n):
      remainder = (int(f_in.readline()) + remainder) % n
    print('NO' if remainder else 'YES')
