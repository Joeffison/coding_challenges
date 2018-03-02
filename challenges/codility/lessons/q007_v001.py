#!/usr/bin/env python3

from util.challenges.array_utils import get_missing_value


def solution(array):
  """
    Checks if array is a sequence containing each element from 1 to N once, and only once.

    Solution with time complexity O(n) and space O(1)
  """
  n = len(array)
  try:
    return 1 if get_missing_value(array) == n + 1 else 0
  except:
    return 0
