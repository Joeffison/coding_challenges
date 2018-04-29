#!/usr/bin/env python3


def solution(array):
  """
  Returns the maximal sum of a double slice.

  Double Slice is a triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N
  and its sum is the sum of the elements between array[X+1] and array[Z-1] minus array[Y]
  """

  n = len(array)
  max_ending = [0] * n
  max_starting = [0] * n

  # finds the sums of the left and the right side of the double slice, respectively
  for i in range(1, n - 1):
    max_ending[i] = max(0, max_ending[i-1] + array[i])
    max_starting[n - 1 - i] = max(0, max_starting[n - i] + array[n - 1 - i])

  # combines the possible sums
  result = 0
  for i in range(1, n - 1):
    result = max(result, max_ending[i-1] + max_starting[i+1])

  return result
