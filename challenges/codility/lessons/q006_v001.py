#!/usr/bin/env python3

from util.challenges.array_utils import get_missing_value


def solution(array):
  """
    Finds the missing element in a given permutation array [1..(N + 1)].

    Solution with time complexity O(n) and space O(1)
  """

  return get_missing_value(array)
