#!/usr/bin/env python3


def solution(n, array):
  """
    Returns n counters after the increment and max operations coded in array
  """

  counters = [0] * n

  # Current greatest value calculated so far
  max_count = 0

  for i in range(len(array)):
    if array[i] == n + 1:
      # max_count = max(counters)
      counters = [max_count] * n
    else:
      counters[array[i] - 1] += 1

      # To avoid calculating max(), we update the max value at each step
      if counters[array[i] - 1] > max_count:
        max_count = counters[array[i] - 1]

  return counters
