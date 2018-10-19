#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n = int(f_in.readline())

  for i in range(n):
    third, third_last, sum = map(int, f_in.readline().split(' '))

    n = int((2 * sum) / (third + third_last))
    factor = int((third_last - third) / (n - 5))

    print(n)
    if factor == 0:
      for j in range(n - 1):
        print(third, end=' ')
      print(third)
    else:
      for j in range(third - (2 * factor), third_last + (2 * factor), factor):
        print(j, end=' ')
      print((third_last + (2 * factor)))
