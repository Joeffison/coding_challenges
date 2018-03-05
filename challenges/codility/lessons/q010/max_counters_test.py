#!/usr/bin/env python3

import random
import unittest

import numpy as np
import timeout_decorator

from challenges.codility.lessons.q010.max_counters_v002 import *

MIN_ELEMENT = 1
MAX_ELEMENT = 100000


class MaxCountersTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual([3, 2, 2, 4, 2], solution(5, [3, 4, 4, 6, 1, 4, 4]))

  # Correctness

  def test_extreme_small(self):
    self.__test_all_max(10, 100)

  def test_single(self):
    array = [random.randint(1, 2) for i in range(40)]
    self.assertEqual([array.count(1)], solution(1, array))

    array = [random.randint(1, 2) for i in range(100)]
    self.assertEqual([array.count(1)], solution(1, array))

  def test_small_random1(self):
    self.__test_random(10, 50, 6)

  def test_small_random2(self):
    self.__test_random(10, 50, 10)

  # Performance

  @timeout_decorator.timeout(0.5)
  def test_medium_random1(self):
    self.__test_random(10, 50, 50)

  @timeout_decorator.timeout(0.5)
  def test_medium_random2(self):
    self.__test_random(10, 50, 500)

  @timeout_decorator.timeout(0.5)
  def test_large_random1(self):
    self.__test_random(50, 100, 2120)

  @timeout_decorator.timeout(0.91)
  def test_large_random2(self):
    self.__test_random(50, 100, 10000)

  def test_extreme_large(self):
    self.__test_extreme_large_p1()
    self.__test_extreme_large_p2()

  @timeout_decorator.timeout(0.93)
  def __test_extreme_large_p1(self):
    self.__test_all_max(50, 10000)

  @timeout_decorator.timeout(0.93)
  def __test_extreme_large_p2(self):
    self.__test_all_max(50, 10000)

  # Utils

  @staticmethod
  def __brute_solution(n, array):
    counters = [0] * n
    # max_count = 0

    for i in range(len(array)):
      if array[i] == n + 1:
        max_count = max(counters)
        counters = [max_count] * n
      else:
        counters[array[i] - 1] += 1

    return counters

  def __test_all_max(self, n, m):
    with self.subTest(n=n, m=m):
      self.assertEqual([0] * n, solution(n, [n + 1] * m))

  def __test_random(self, n, m, n_max_counter):
    array = list(np.random.random_integers(1, n, m))
    array += [n + 1] * n_max_counter
    random.shuffle(array)

    with self.subTest(n=n, m=m + n_max_counter, n_max_counter=n_max_counter):
      self.assertEqual(self.__brute_solution(n, array), solution(n, array))

if __name__ == '__main__':
  unittest.main()
