#!/usr/bin/env python3


def solution(array):
  """
  Finds the smallest positive integer not in array.
  The smallest possible answer is 1.

  :param array: list of integers
  :return: smallest positive integer not in array.
  """

  # smallest answer so far
  i = 1

  # visited values
  visited = []

  for value in array:
    visited.append(value)
    # if i is equal to value,
    # we have to increment it before we visit the next item in array.
    if value == i:
      # we have to increment i to a number that we did not visit before.
      while True:
        value += 1
        if value not in visited:
          break
      i = value
  return i
