#!/usr/bin/env python3


def sum_first_n_natural_numbers(n):
  return n * (n + 1) // 2


class InvalidInputException(Exception):
  pass


def get_missing_value(array):
  """
    Finds the missing element in a given permutation of [1..(N + 1)].
    Assumes no duplicated values in array.

    Solution with time complexity O(n) and space O(1)
  """

  n = len(array)

  # values can be up to n + 1
  array += [n + 2]

  # As no value v in array is repeated,
  # we mark it as visited by setting the v-indexed value as negative
  for i in range(n):
    v_index = abs(array[i]) - 1
    if v_index > len(array):
      raise InvalidInputException()
    array[v_index] = -array[v_index]

  # The only index with a positive value represents an unvisited (thus missing) number
  for i in range(len(array)):
    if array[i] > 0:
      return i + 1
