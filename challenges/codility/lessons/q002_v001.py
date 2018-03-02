#!/usr/bin/env python3


def solution(array):
  """
    Returns the only number occurring k times, given k is an odd number.
  """

  # x XOR x = 0
  # x XOR y = z, with bit 1 in the positions where only x or y has 1
  # x XOR 0 = x
  response = 0

  for i in array:
    # Intermediate values of response might not be in array,
    # because of conflicting bits 1 in two neighbor elements,
    # but it won't be a problem
    # because at least one of the two elements is repeated in array
    # (by the end, only the bits in the odd occurring element will be left)
    response ^= i

  return response
