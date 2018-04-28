#!/usr/bin/env python3


def solution(array):
  """
  Returns the maximal sum of a slice of array.
  """

  # we keep track of what is the biggest number, to make sure not to return 0 when there is only negative numbers
  max_item = -1000000

  max_ending = max_slice = 0
  for a in array:
    max_item = max(max_item, a)
    max_ending = max(0, max_ending + a)
    max_slice = max(max_slice, max_ending)

  # if we only have negative numbers, we return the maximum value
  if max_item < 0:
    return max_item

  return max_slice
