#!/usr/bin/env python3

import fileinput
import sys


if __name__ == '__main__':
  f_in = fileinput.input()

  n, k = map(int, f_in.readline().split())
  count = 0
  for line in f_in:
    count += (int(line) % k == 0)
  sys.stdout.write(str(count))
