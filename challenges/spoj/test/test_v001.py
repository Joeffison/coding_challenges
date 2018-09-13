#!/usr/bin/env python3

import fileinput


if __name__ == '__main__':
  for line in fileinput.input():
    n = int(line)
    if n == 42: break
    print(n)
