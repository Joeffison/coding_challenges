#!/usr/bin/env python3

import fileinput
from math import sqrt

if __name__ == '__main__':
  for n in fileinput.input():
    if n[0] == '-':
      break
    elif n[-2] in ['1', '7', '9']:
      n = int(n)
      beehive_factor = (3 + sqrt(12*n - 3))/6.0
      if beehive_factor == int(beehive_factor):
        print('Y')
      else:
        print('N')
    else:
      print('N')
