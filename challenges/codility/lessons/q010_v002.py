#!/usr/bin/env python3


def solution(n, array):
  """
    Returns n counters after the increment and max operations coded in array.

    It iterates over array once and over the counters once, thus the time complexity is O(n + m)
  """

  counters = [0] * n

  # Current greatest value calculated so far
  max_count = 0

  # Value in max when the last max operation was found in array
  last_max_value = 0

  for i in range(len(array)):
    if array[i] == n + 1:
      # when a max operation is demanded, we simply save the current max value
      # to use it in future increments
      last_max_value = max_count
    else:
      if counters[array[i] - 1] < last_max_value:
        # As we don't update all counters when we find a max operation,
        # we have to increment considering last_max_value
        counters[array[i] - 1] = last_max_value + 1
      else:
        counters[array[i] - 1] += 1

      # To avoid calculating max(), we update the max value at each step
      if counters[array[i] - 1] > max_count:
        max_count = counters[array[i] - 1]

  # As we don't update all counters when we find a max operation,
  # we have to make sure to update all counters we didn't already update
  return [max(i, last_max_value) for i in counters]
