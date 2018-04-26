#!/usr/bin/env python3


def solution(array):
  """
  Finds max(array[p] - array[q]), given n = len(array) and 0 <= q < p < n
  """

  result = 0

  # if array has less than 2 elements, the result is always 0
  if len(array) > 1:

    # current min value
    min_value = array[0]

    for item in array:
      slice_result = item - min_value

      if slice_result < 0:
        # if the difference is negative, item is smaller than the current min_value
        min_value = item
      elif slice_result > result:
        result = slice_result

  return result
