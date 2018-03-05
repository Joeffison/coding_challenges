#!/usr/bin/env python3


def solution(array, n_rotations):
  """
  Returns the Cyclic Rotation of array with n_rotations positions to the right.
  """

  n = len(array)
  n_rotations = n_rotations % n if n > 0 else 0
  return array[n - n_rotations:] + array[:n - n_rotations]
