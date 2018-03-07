#!/usr/bin/env python3


def solution(array):
  """
  Finds the slice (with at least 2 elements) of array with the minimal average.
  There is a mathematical proof showing that any slice S' with more than 3 elements and average A
  can be divided into slices of size 2 and/or three with average smaller or equal than A.

  Time Complexity: O(n)
  Space Complexity: O(1)

  :param array: Array with at least 2 elements
  :return: Starting position of slice with the minimal average.
  """

  min_avg = (array[0] + array[1]) / 2.0
  min_pos = 0

  for i in range(0, len(array) - 2):
    current_sum = array[i] + array[i + 1]
    current_avg = current_sum / 2.0
    if current_avg < min_avg:
      min_avg = current_avg
      min_pos = i

    current_avg = (current_sum + array[i + 2]) / 3.0
    if current_avg < min_avg:
      min_avg = current_avg
      min_pos = i

  if (array[-2] + array[-1]) / 2.0 < min_avg:
    min_pos = len(array) - 2

  return min_pos
