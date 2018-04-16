#!/usr/bin/env python3
from util.challenges.array_challenges import get_leader


def solution(array):
  n = len(array)
  leader, indexes = get_leader(array)
  n_leader = len(indexes)

  count = 0
  for i in range(n_leader - 1):
    for j in range(indexes[i], indexes[i+1]):
      if (i + 1) > (j + 1)/2 and (n_leader - i - 1) > (n - j - 1)/2:
        count += 1
  return count
