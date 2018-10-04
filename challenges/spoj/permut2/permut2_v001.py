#!/usr/bin/env python3

import fileinput
import sys


if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange


def is_ambiguous(array, n):
  for i in range(n):
    if array[array[i]] != i:
      return False
  return True


# already decreasing 1 to simplify checks and minimizes the subtractions to 50%
def cast_input(s):
  return int(s) - 1


if __name__ == '__main__':
  f_in = fileinput.input()
  while True:
    n = f_in.readline()
    if n[0] == '0':
      break
    else:
      n = int(n)

    if is_ambiguous(map(cast_input, f_in.readline().split()), n):
      print('ambiguous')
    else:
      print('not ambiguous')
