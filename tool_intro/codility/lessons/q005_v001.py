#!/usr/bin/env python3

import math


def solution(x, y, jump_size):
  """
    Returns the minimum number of times to add jump_size to x
    in order to reach y.

    Solution in O(1) for "Frog Jump".
  """
  return math.ceil((y - x) / jump_size)
