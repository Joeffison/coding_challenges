#!/usr/bin/env python3


def solution(array):
  """
    Determine whether a triangle can be built from a given set of edges.

    Time Complexity O(n*log(n)), because we sort the array.
    Space Complexity O(1).
  """
  if len(array) > 2:
    array.sort()

    # assuming a, b, c as potential sides of a triangle, we sort the array so we can assume:
    # given c > b > a:
    #  - we have c > a and b > a, then we derive c = a + k1 and b = a + k2, with k1 > 0 and k2 > 0,
    #       so (a + k1) + (a + k2) = 2a + k1 + k2 (which is greater than a),
    #       so follows that b + c > a (first triangle condition is true)
    #
    #  - the second triangle condition is c + a > b. From the first premise, we have c = b + k3, with k3 > 0
    #     - first case, a > 0:
    #       c + a = (b + k3) + a = b + (k3 + a), as k3 + a > 0 we have b + (k3 + a) > b and we derive that c + a > b
    #     - second case, a < 0:
    #       so c + a = (b + k3) + a = b + (k3 + a), to have c + a > b, we need k3 + a > 0
    #       assuming that a + b > c (third triangle condition):
    #       we have a + b > b + k3 =>  a + b - b > k3 => a > k3, which combined with k3 > 0 gives us that a > k3 > 0,
    #       thus a > 0, which is a contradiction with our assumption a < 0.
    #       So, we can assume that if the third triangle condition is true, a > 0 and the second condition is also true.
    for i in range(len(array) - 2):
      if array[i] + array[i + 1] > array[i + 2]:
        return 1
  return 0
