#!/usr/bin/env python3
from util.challenges.array_challenges import __count_total


def __class_based_prefix_sums(array, classes):
  """
  Given N = len(array) and M = len(classes):

  Imagine that array is split into M different lists of length N,
  for each list l, l[i][k] == 1 iff array[k] == classes[i], 0 otherwise.

  This method returns the prefix_sum for each list l explained above.
  """

  n = len(array)
  m = len(classes)

  sums = [[0] * (n + 1) for i in range(m)]

  for i in range(n):
    for j in range(m):
      if array[i] == classes[j]:
        sums[j][i + 1] = sums[j][i] + 1
      else:
        sums[j][i + 1] = sums[j][i]

  return sums


def __class_is_present(prefix_sums, class_index, start_pos, end_pos):
  return __count_total(prefix_sums[class_index], start_pos, end_pos) > 0


def solution(s, start_pos, end_pos):
  """
  Find the minimal nucleotide from a range of sequence DNA.

  :param s: String consisting of the letters A, C, G and T,
    which correspond to the types of successive nucleotides in the sequence
  :param start_pos: array with the start indexes for the intervals to check
  :param end_pos: array with the end indexes for the intervals to check

  :return: a list with the minimal nucleotide for each interval defined by start_pos and end_pos
  """

  highest_class = 'T'
  highest_class_value = 4
  # The array below must be in ascending order regarding the value assigned to the classes in the challenge description
  # (not necessarily in alphabetic order)
  other_classes = ['A', 'C', 'G']
  other_classes_values = [1, 2, 3]

  # We create a prefix_sum list for each class, so we can identify when a range has that specific class
  prefix_sums = __class_based_prefix_sums(s, other_classes)
  result = []

  for i in range(len(start_pos)):
    # We don't need to create a prefix_sum list for the class with highest value,
    # because we can always use it as a fallback
    current_result = highest_class_value

    for j in range(len(other_classes)):
      if __class_is_present(prefix_sums, j, start_pos[i], end_pos[i]):
        current_result = other_classes_values[j]
        break

    result.append(current_result)

  return result
