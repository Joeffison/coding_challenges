#!/usr/bin/env python3

from itertools import permutations

import numpy as np
from scipy.spatial.distance import pdist


def distance(x1, y1, x2, y2):
  """
    The Squared Euclidean Distance is given by the following formula:
    round(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
  """
  return pdist(np.array([[x1, y1], [x2, y2]]), metric='sqeuclidean')


def solution(A, B, C, D):
  """
    Finds the maximum squared distance between two points,
    created assigning the integers A, B, C and D to the coordinates
    (A, B, C and D must be used one time each).
  :return:
    Maximum squared distance for points created with A, B, C and D (used one time each).
  """

  # Creates all possible permutations
  p_array = permutations([A, C, D, B], 4)

  # Calculates the distance for each permutation
  distances = [distance(*pairs) for pairs in p_array]

  # Returns the maximum distance
  return max(distances)
