#!/usr/bin/env python3
from util.data_structures import Stack


def solution(sizes, directions):
  """
  Counts the number of fish alive after all possible meetings
  """

  DOWNSTREAM = 0

  # number of fish going downstream that won't meet bigger fish
  alive = 0

  # fish going upstream
  upstream = Stack()

  for i in range(len(directions)):
    if directions[i] == DOWNSTREAM:
      alive += 1
      while upstream.length():
        # the current fish will eat any fish going upstream which is smaller than the current fish
        fish_upstream = upstream.pop()

        # if we find any fish going upstream bigger than the current fish, the current fish will be eaten
        if sizes[fish_upstream] > sizes[i]:
          alive -= 1

          # the fish that ate the current fish must stay in the stack
          upstream.push(fish_upstream)

          # we move to the next fish
          break
    else:
      # we store fish going upstream because we may find other fish going downstream
      # (and we will have to decide which fish eats which)
      upstream.push(i)

  # sum the alive fish going downstream and upstream
  return alive + upstream.length()
