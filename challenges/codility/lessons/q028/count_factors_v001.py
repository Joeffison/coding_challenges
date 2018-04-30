#!/usr/bin/env python3

from math import sqrt


def solution(n):
  """
  
  :param n:
  :return:
  """

  result = 1
  r = int(sqrt(n))

  for i in range(2, r + 1):
    result += (n%i==0)*2

  return result + (r*r != n)
