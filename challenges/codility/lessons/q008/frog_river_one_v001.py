#!/usr/bin/env python3


def solution(desired_position, array):
  """
    Finds max(i), given i: the index of first occurrence for the values in 1..desired_position
  """

  if desired_position > len(array):
    return -1

  path = [-1] * (desired_position)

  for i in range(len(array)):
    if array[i] <= desired_position and (path[array[i] - 1] == -1 or i < path[array[i] - 1]):
      path[array[i] - 1] = i

  max = 0
  for i in range(len(path)):
    if path[i] < 0:
      return -1
    elif path[i] > max:
      max = path[i]

  return max
