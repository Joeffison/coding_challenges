#!/usr/bin/env python3

import fileinput
import sys


def solution(a, b, c):
  remainder = c - b
  if remainder == (b - a):
    return "AP " + str(c + remainder)
  return "GP " + str(c * (c / b))


if __name__ == '__main__':
  f_in = fileinput.input()
  while True:
    a, b, c = map(int, f_in.readline().split())
    if a == 0 and b == 0 and c == 0:
      break
    print(solution(a, b, c))
