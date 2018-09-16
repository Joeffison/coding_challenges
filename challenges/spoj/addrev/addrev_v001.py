#!/usr/bin/env python2

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()

  n_test_cases = int(f_in.readline())

  for test_case in range(n_test_cases):
    print(int(str(sum(map(lambda x: int(x[::-1]), f_in.readline().split())))[::-1]))
