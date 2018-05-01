#!/usr/bin/env python3

from math import sqrt


def solution(n):
  """
  Returns the minimal perimeter for a rectangle of area n.
  """

  # given the sides a and b, the area of a rectangle is n = a*b and the perimeter is 2 * (a + b)
  # for a minimal perimeter, we have to minimize the difference between a and b
  for i in range(int(sqrt(n)), 0, -1):

    # a and b must be the closest possible to sqrt(n)
    if n % i == 0:
      return 2*(i + n//i)
