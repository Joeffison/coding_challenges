#!/usr/bin/env python2

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())
  max_value = 1000007

  for i in range(n_test_cases):
    n = int(f_in.readline())
    print('%d' % ((n*(3*n + 1)/2) % max_value))
