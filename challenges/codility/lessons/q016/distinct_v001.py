#!/usr/bin/env python3


def solution(array):
  """
    Computes number of distinct values in an array.
  """

  # Sets only have distinct values
  # and creating a set from a list has a good time complexity, as it uses hash tables
  return len(set(array))
