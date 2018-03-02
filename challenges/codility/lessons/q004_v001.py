#!/usr/bin/env python3


def solution(array):
  """
    When splitting the array in two parts a and b,
    with array = a + b,
    returns the minimal difference that can be achieved between
    the sum of elements in a and
    the sum of elements in b.

    Solution using Dynamic Programming.
  """

  # left_side[i] is the sum of elements in array from index 0 up to i
  left_side = [None] * (len(array)-1)

  # right_side[i] is the sum of elements in array from index i + 1 up to n - 1
  right_side = [None] * (len(array)-1)

  # We initialize the left side array with the first element and the right side with the last element
  left_side[0] = array[0]
  right_side[len(array) - 2] = array[len(array) - 1]

  # Storing all sums for the left and right side, to use the last calculated value to calculate the next sum
  for i in range(1, len(array)-1):
    left_side[i] = left_side[i - 1] + array[i]
    right_side[len(array) - i - 2] = right_side[len(array) - i -1] + array[len(array) - i - 1]

  # Finally, returns the minimal value for the given function
  return min([abs(left_side[i] - right_side[i]) for i in range(len(array) - 1)])
