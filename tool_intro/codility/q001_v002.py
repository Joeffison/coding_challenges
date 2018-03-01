#!/usr/bin/env python3


def replace_negative(l, default_value=0):
  """
  Replaces all negative values with default_value

  :param l: Original list
  :param default_value: The value to replace negatives values with. Default is 0.
  :return: Number of values replaced
  """
  n_replaced = 0

  for i in range(len(l)):
    if l[i] < 0:
      l[i] = default_value
      n_replaced += 1

  return n_replaced


def solution(A):
  """
  Finds the smallest positive integer not in A.
  The smallest possible answer is 1.

  :param A: list of integers
  :return: smallest positive integer not in A.
  """
  length = len(A)

  # When there is no positive value in A, default answer is 1
  if replace_negative(A) is length:
    return 1

  for value in A:
    # We mark a value v as visited by setting the value indexed by v as negative
    # We can ignore v, when it is out of the range,
    # because it means that v > N, thus there is a 0 < x < v and x < N and x not in A.
    if (value is not 0) and (abs(value) - 1 < length) and (A[abs(value)-1] >= 0):
      A[abs(value) - 1] = -A[abs(value) - 1] if A[abs(value) - 1] is not 0 else -1

  # The first index v with a positive value found means that
  # v + 1 is not in A (otherwise we would have visited and marked it as negative)
  for i in range(length):
    if A[i] >= 0:
      return i + 1

  # when A contains all numbers between 1 and N, we must return N + 1
  return length + 1
