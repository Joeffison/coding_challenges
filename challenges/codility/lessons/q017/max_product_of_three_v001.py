#!/usr/bin/env python3


def solution(array):
  """
    Returns the value of the maximal product of three values in an array.
  """

  array.sort()

  # For the maximal product, we might have to multiply two negative values,
  # that is why we compare the product of the three biggest elements with
  # the product of the biggest element and the two smallest elements
  return max(array[-1] * array[-2] * array[-3], array[-1] * array[0] * array[1])
