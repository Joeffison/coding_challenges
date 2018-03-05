#!/usr/bin/env python3


def solution(array):
  """
    Finds the number of combinations (ai, aj), given:
     - ai == 0
     - aj == 1
     - j > i

    Time Complexity: O(n), as we go through the array only once (in reverse order)
    Space Complexity O(1), as we store three variables and create one iterator
  """
  result = 0
  count = 0

  # We iterate over array in reverse order to reuse the counter of 1s
  for i in range(len(array) - 1, -1, -1):
    if array[i] == 1:
      count += 1
    else:
      if result + count > 1000000000:
        return -1

      # We never reset "count", as we need to sum the number of all 1s after each 0
      result += count

  return result
