#!/usr/bin/env python3


def solution(array):
  """
    Finds the missing element in a given permutation array [1..(N + 1)].

    Solution with time complexity O(n) and space O(1)
  """

  n = len(array)

  # values can be up to n + 1
  array += [n + 2]

  # As no value v in array is repeated,
  # we mark it as visited by setting the v-indexed value as negative
  for i in range(n):
    array[abs(array[i]) - 1] = -array[abs(array[i]) - 1]

  # The only index with a positive value represents an unvisited (thus missing) number
  for i in range(len(array)):
    if array[i] > 0:
      return i + 1
