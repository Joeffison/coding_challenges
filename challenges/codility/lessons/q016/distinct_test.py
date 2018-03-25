#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q016.distinct_v001 import *

MAX_N = 100000
MIN_ELEMENT = -1000000
MAX_ELEMENT = 1000000


class DistinctTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(3, solution([2, 1, 1, 2, 3, 1]))

  # Correctness

  def test_extreme_empty(self):
    # empty sequence
    self.assertEqual(0, solution([]))

  def test_extreme_single(self):
    # sequence of one element
    self.assertEqual(1, solution([2]))
    self.assertEqual(1, solution([0]))

  def test_extreme_two_elems(self):
    # sequence of two distinct elements
    self.assertEqual(2, solution([2, 1]))

  def test_extreme_one_value(self):
    # sequence of 10 equal elements
    self.assertEqual(1, solution([10]*10))

  def test_extreme_negative(self):
    # sequence of negative elements, length=5
    self.assertEqual(4, solution([-1, MIN_ELEMENT, MIN_ELEMENT, -2, -3]))

  def test_extreme_big_values(self):
    # sequence with big values, length=5
    n = 5
    self.assertEqual(n, solution([MAX_ELEMENT - i for i in range(n)]))

  def test_medium1(self):
    # chaotic sequence of values from [0..1K], length=100
    self.__test_chaotic(100, 0, 1000)

  def test_medium2(self):
    # chaotic sequence of values from [0..1K], length=200
    self.__test_chaotic(200, 0, 1000)

  def test_medium3(self):
    # chaotic sequence of values from [0..10], length=200
    self.__test_chaotic(200, 0, 10)

  # Performance

  def test_large1(self):
    # chaotic sequence of values from [0..100K], length = 10K
    self.__test_chaotic(10000, 0, 100000)

  def test_large_random1(self):
    # chaotic sequence of values from [-1M..1M], length=100K
    self.__test_chaotic(MAX_N, MIN_ELEMENT, MAX_ELEMENT)

  def test_large_random2(self):
    # another chaotic sequence of values from [-1M..1M], length=100K
    self.__test_chaotic(MAX_N, MIN_ELEMENT, MAX_ELEMENT)

  # Utils

  @staticmethod
  def __brute_solution(array):
    if array:
      array.sort()

      count = 1
      for i in range(1, len(array)):
        if array[i] != array[i - 1]:
          count += 1

      return count
    else:
      return 0

  def __test_sequence(self, n=100, shuffled=True):
    l = list(range(n))

    if shuffled:
      random.shuffle(l)

    with self.subTest(n=n):
      self.assertEqual(n, solution(l))

  def __test_chaotic(self, n, min_value, max_value):
    array = list(np.random.random_integers(min_value, max_value, n))

    with self.subTest(n=n):
      self.assertEqual(self.__brute_solution(array), solution(array))

if __name__ == '__main__':
  unittest.main()
