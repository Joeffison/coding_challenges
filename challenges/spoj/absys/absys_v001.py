#!/usr/bin/env python2

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  n = int(f_in.readline())
  machula = 'machula'

  for i in range(n):
    f_in.readline() # trashes the empty line
    a, _, b, _, c = f_in.readline().split(' ')

    if machula in a:
      c = int(c)
      a = c - int(b)
    elif machula in b:
      c = int(c)
      b = c - int(a)
    else:
      c = int(a) + int(b)

    print('{a} + {b} = {c}'.format(a=a, b=b, c=c))
