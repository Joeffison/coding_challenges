#!/usr/bin/env python2

import fileinput

MAX_N = 10000000


if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  x = [1, 1, 2, 3]
  y = [1, 2, 1, 1]
  processed = len(x)
  direction = 1

  for i in range(n_test_cases):
    n = int(f_in.readline())

    while n > processed:
      x.append(x[-1] - direction)
      y.append(y[-1] + direction)
      processed += 1

      if x[-1] == 1:
        x.append(1)
        y.append(y[-1] + 1)
        direction = -1
        processed += 1
      elif y[-1] == 1:
        x.append(x[-1] + 1)
        y.append(1)
        direction = 1
        processed += 1

    print('TERM {n} IS {x}/{y}'.format(n=n, x=x[n - 1], y=y[n - 1]))
