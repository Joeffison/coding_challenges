#!/usr/bin/env python3


def  oddNumbers(l, r):
  """
  List odd numbers within a closed interval.
  :param l: left interval endpoint (inclusive)
  :param r: right interval endpoint (inclusive)
  :return: odd numbers within [l, r].
  """
  l = l if l % 2 == 1 else l + 1
  r = r if r % 2 == 0 else r + 1
  return list(range(l, r, 2))

"""
#!/bin/python3

import sys
import os

# Complete the function below.

def  oddNumbers(l, r):


f = open(os.environ['OUTPUT_PATH'], 'w')


_l = int(input());


_r = int(input());

res = oddNumbers(_l, _r)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()
"""
