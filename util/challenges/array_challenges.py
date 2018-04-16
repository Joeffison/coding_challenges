#!/usr/bin/env python3


def sum_first_n_natural_numbers(n):
  return n * (n + 1) // 2


class InvalidInputException(Exception):
  pass


def get_missing_value(array):
  """
    Finds the missing element in a given permutation of [1..(N + 1)].
    Assumes no duplicated values in array.

    Problem Name: Permutation's Missing Element
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


def __prefix_sums(array):
  n = len(array)
  sums = [0] * (n + 1)
  for k in range(1, n + 1):
    sums[k] = sums[k - 1] + array[k - 1]
  return sums


def __count_total(sums, x, y):
  return sums[y + 1] - sums[x]


def count_max_mushrooms(array, k, m):
  """
    Finds the max sum of elements that can be visited from k, using m moves.

    Problem Name: Mushroom picker
    The total time complexity of such a solution is O(n + m).

  :param array: n integers (1 <= n <= 100,000)
  :param k: Initial Position
  :param m: Number of Moves
  :return: Max sum of elements that can be visited from k, using m moves.
  """

  n = len(array)
  result = 0
  pref = __prefix_sums(array)

  # Let's
  for p in range(min(m, k) + 1):
    left_pos = k - p
    right_pos = min(n - 1, max(k, k + m - 2 * p))
    result = max(result, __count_total(pref, left_pos, right_pos))

  for p in range(min(m + 1, n - k)):
    right_pos = k + p
    left_pos = max(0, min(k, k - (m - 2 * p)))
    result = max(result, __count_total(pref, left_pos, right_pos))

  return result


def get_leader(array):
  n = len(array)
  size = 0
  for k in range(n):
    if (size == 0):
      size += 1
      value = array[k]
    else:
      if (value != array[k]):
        size -= 1
      else:
        size += 1

  candidate = -1
  if (size > 0):
    candidate = value

  count = 0
  indexes = []
  for k in range(n):
    if (array[k] == candidate):
      count += 1
      indexes.append(k)
  if (count > n // 2):
    return candidate, indexes
  return -1, []
