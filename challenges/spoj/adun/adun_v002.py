#!/usr/bin/env python3

import fileinput
import sys


if __name__ == '__main__':
  f_in = fileinput.input()

  sys.stdout.write(str(
    int(f_in.readline()) +
    int(f_in.readline())
  ))
