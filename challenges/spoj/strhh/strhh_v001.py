#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    word = f_in.readline()
    print(word[:int((len(word) - 1)/2):2])
