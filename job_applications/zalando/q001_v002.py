#!/usr/bin/env python3

import numpy as np
from scipy.spatial.distance import pdist
from sympy.utilities.iterables import multiset_permutations


def distance(x1, y1, x2, y2):
  """
    The Squared Euclidean Distance is given by the following formula:
    round(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
  """
  return pdist(np.array([[x1, y1], [x2, y2]]), metric='sqeuclidean')


def distance_for_array(array):
  return distance(*array)


def solution(A, B, C, D):
  """
    Finds the maximum squared distance between two points,
    created assigning the integers A, B, C and D to the coordinates
    (A, B, C and D must be used one time each).
  :return:
    Maximum squared distance for points created with A, B, C and D (used one time each).
  """

  # Creates all possible permutations
  p_array = list(multiset_permutations(np.array([A, B, C, D])))

  # Calculates the distance for each permutation
  distances = np.apply_along_axis(distance_for_array, 1, p_array)

  # Returns the maximum distance
  return np.nanmax(distances)
