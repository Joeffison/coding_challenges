#!/usr/bin/env python3

from operator import itemgetter


def solution(array):
  """
  Computes the number of intersections of closed intervals

  Time Complexity: O(n*log(n)), given n = len(array),
    because we sort the list of endpoints in O(2n*log(2n)) and iterate over it in O(2n):
    O(2n*log(2n) + 2n) is a function of the class O(n*log(n)).

  Space Complexity: O(n), because we create a list of endpoints and 5 other variables (including 'i') in O(2n + 5).

  :param array:
    list [a1, a2, ..., an], item ai represents a closed interval with center i and size 2*list[i], i.e,
    represent the interval [x, y], given x = i - list[i] and y = i + list[i]

  :return:
    number of intersections if it does not exceed 10,000,000, and returns -1 otherwise
  """

  LEFT = 0
  RIGHT = 1

  # creates a list with all the endpoints (left and right) as separate elements
  endpoints = []
  for i in range(len(array)):
    endpoints.append({'value': i - array[i], 'side': LEFT})
    endpoints.append({'value': i + array[i], 'side': RIGHT})

  # sorts the endpoints, but making sure the left sides come first
  endpoints.sort(key=itemgetter('value', 'side'))

  response = 0

  # represents the number of potential inner intersections
  # (it starts with -1, so it can become 0 on the first left side)
  inner_candidates = -1

  for i in range(len(endpoints)):
    # when we see a new interval opening, we increment the number of possible inner intersections
    if endpoints[i]['side'] == LEFT:
      inner_candidates += 1

      # and if this number is greater than 0 (we saw at least one interval opening after the last non-ended interval)
      # it means that we saw an interval starting inside of another
      if inner_candidates > 0:
        response += inner_candidates

        if response > 10000000:
          return -1
    else:
      inner_candidates -= 1

  return response
