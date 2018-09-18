#!/usr/bin/env python3

import fileinput

dp_fctrl = [1, 2, 6, 24, 120]


def fctrl(n):
  if n == 0:
    return 1

  for i in range(len(dp_fctrl) + 1, n + 1):
    dp_fctrl.append(dp_fctrl[-1] * i)

  return dp_fctrl[n - 1]


if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    print(fctrl(int(f_in.readline())))
