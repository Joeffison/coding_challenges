#!/usr/bin/env python3


def ignore(S, i, j):
  """
    Ignores brackets that are irrelevant
    on the left and on the right side
  """
  while (i < j-1) and (S[i + 1] == ')'):
    i = i + 1

  while (i < j-1) and (S[j - 1] == '('):
    j = j - 1

  return i, j


def walk(i, j):
  """
    Walks through the String without crossing the boundaries,
    making sure that i < j-1
  """
  if i < j - 1:
    i = i + 1
    # It is necessary to check again if i < j-1, after we incremented i
    if i < j - 1:
      j = j - 1

  return i, j


def solution(S):
  """
    Splits a string S into two parts (left and right),
    such that the number of opening brackets in the left part is equal to
    the number of closing brackets in the right part.

    As we don't visit the same character index in S twice,
    our time complexity is O(N).

    We only require the additional space for the int variables i and j
    within solution() and either ignore() or walk() scope,
    i.e. 4 is a constant and is under space complexity class O(1).
  """

  i = -1
  j = len(S)
  while i < j - 1:
    i, j = ignore(S, i, j)
    i, j = walk(i, j)
  return i + 1
