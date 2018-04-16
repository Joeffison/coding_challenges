#!/usr/bin/env python3
from util.challenges.array_challenges import get_leader


def solution(array):
  leader, indexes = get_leader(array)
  if len(indexes) > (len(array) // 2):
    return indexes[0]
  else:
    return -1
