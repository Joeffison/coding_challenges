#!/usr/bin/env python3

import fileinput


if __name__ == '__main__':
  f_in = fileinput.input()

  for n in range(10):
    apples = int(f_in.readline())
    difference = int(f_in.readline())
    person2 = (apples // 2) - (difference // 2)
    print(apples - person2)
    print(person2)
