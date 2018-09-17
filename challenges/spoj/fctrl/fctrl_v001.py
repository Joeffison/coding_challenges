#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    n = int(f_in.readline())

    result = 0
    remainder = n
    while True:
      remainder = int(remainder/5)
      if remainder == 0:
        break
      result += remainder
    print(result)
