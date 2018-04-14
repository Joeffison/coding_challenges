#!/usr/bin/env python3
from util.data_structures import Stack


def solution(array):
  """
  Given an array A of N positive integers specifying the height of the wall,
  returns the minimum number of blocks needed to build it.
  """

  # We use a stack because if we need a block of height h and in a previous iteration, we used one of height h':
  # a) given h' == h  we can reuse it
  # b) given h' > h we need it to not reach the place we will put the current block
  # c) given h' < h we can build a new block of height (h - h') on top of it
  stack = Stack()

  # number of blocks used
  blocks = 0

  for item in array:

    # Firstly, we remove all blocks taller the the one we need
    while stack.length() and stack.tail()[-1] > item:
      stack.pop()

    # Then we only build a new block, if we don't have one with the same height
    if stack.length() < 1 or stack.tail()[-1] < item:
      stack.push(item)
      blocks += 1

  return blocks
