#!/usr/bin/env python3
from util.data_structures import Stack


def solution(sizes, directions):
  DOWNSTREAM = 0
  UPSTREAM = 1

  stack = Stack()
  current_index = 0
  alive_fish = 0

  for fish in directions:
    current_index += 1
    if fish == DOWNSTREAM:
      alive_fish += 1
    else:
      stack.push(current_index - 1)
      break

  for i in range(current_index, len(directions)):
    if directions[i] == UPSTREAM:
      stack.push(i)
    else:
      alive_fish += 1
      while stack.length():
        fish_upstream = stack.pop()
        if sizes[fish_upstream] > sizes[i]:
          stack.push(fish_upstream)
          alive_fish -= 1
          break

  return alive_fish + stack.length()
