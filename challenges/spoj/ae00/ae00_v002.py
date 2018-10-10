#!/usr/bin/env python3

import fileinput
import math

if __name__ == '__main__':
  n = int(fileinput.input().readline())

  result = 0
  for i in range(int(math.sqrt(n))):
    result += n // (i + 1) - i

  print(result, end='')
