#!/usr/bin/env python3

import math


def solution(A, B, K):
  """
    Returns the number of integers within the range [A..B] that are divisible by K
  """
  first = math.ceil(A / K) * K

  if first > B:
    return 0

  last = math.floor(B / K) * K

  return ((last - first) // K) + 1
