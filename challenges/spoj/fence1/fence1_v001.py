#!/usr/bin/env python3

import fileinput
import math


if __name__ == '__main__':
  factor = 1 / (2. * math.pi)

  for n in fileinput.input():
    n = int(n)
    if n == 0:
      break

    print('%.2f' % (math.pow(n, 2)*factor))
