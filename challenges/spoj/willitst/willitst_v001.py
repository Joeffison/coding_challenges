#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  for n in fileinput.input():
    n = int(n)
    if n & (n - 1):
      print("NIE")
    else:
      print("TAK")
