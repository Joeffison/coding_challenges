#!/usr/bin/env python3
from util.data_structures import Stack


def solution(s):
  """
  Check if a string has properly matching brackets

  :param s: String to verify if it is well-formed
  :return: 1 if the brackets are properly matching, 0 otherwise
  """

  OPENING = "([{"
  CLOSING = ")]}"
  stack = Stack()

  for item in s:
    # Stores any opening character
    if item in OPENING:
      stack.push(item)
    else:
      # if a closing bracket is found and we try to remove the matching opening bracket from the top of the stack
      # in case the top of the stack is not a matching bracket, the string is not properly nested
      if stack.length() < 1 or stack.pop() is not OPENING[CLOSING.index(item)]:
        return 0

  return 0 if stack.length() > 0 else 1
