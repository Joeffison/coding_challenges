#!/usr/bin/env python3


def findNumber(arr, k):
  """
  Check if number is in a list.
  :param arr: list to verify
  :param k: element to look for
  :return: YES, if k is in arr. NO, otherwise.
  """
  return 'YES' if k in arr else 'NO'

"""
#!/bin/python3

import sys
import os


def findNumber(arr, k):


f = open(os.environ['OUTPUT_PATH'], 'w')

_arr_cnt = 0
_arr_cnt = int(input())
_arr_i = 0
_arr = []
while _arr_i < _arr_cnt:
  _arr_item = int(input());
  _arr.append(_arr_item)
  _arr_i += 1

_k = int(input());

res = findNumber(_arr, _k)
f.write(res + "\n")

f.close()
"""
