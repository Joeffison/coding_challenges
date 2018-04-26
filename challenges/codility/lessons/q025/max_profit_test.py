#!/usr/bin/env python3

import unittest

import numpy as np
import timeout_decorator

from challenges.codility.lessons.q025.max_profit_v001 import *

MAX_N = 400000
MIN_ELEMENT = 0
MAX_ELEMENT = 200000


class MaxProfitTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(356, solution([23171, 21011, 21123, 21366, 21013, 21367]))

  # Correctness

  def test_simple_desc(self):
    # descending and ascending sequence, length=5
    n = 5
    self.__test_sequence(n)
    self.__test_sequence(n, False)

  def test_simple_empty(self):
    # empty and [0,200000] sequence
    self.__subtest(0, [], n=0)
    self.__test_sequence(MAX_ELEMENT)

  def test_two_hills(self):
    # two increasing subsequences
    n = 20
    m = n * 2
    self.__subtest(m-1, list(range(n)) + list(range(m)), n=n+m)

  def test_max_profit_after_max_and_before_min(self):
    # max profit is after global maximum and before global minimum
    n = 20
    self.__subtest(n-1, [MAX_ELEMENT - 1, MAX_ELEMENT] + list(range(n)) + [0], n=n+3)

  # Performance

  @timeout_decorator.timeout(0.550)
  def test_medium_1(self):
    # large value (99) followed by short V-pattern (values from [1..5]) repeated 100 times
    n = 5
    l = list(range(1, n+1))
    self.__subtest(n-1, [99] + (l * 100), n=len(l)*100 + 1)

  @timeout_decorator.timeout(0.550)
  def test_large_1(self):
    # large value (99) followed by short pattern (values from [1..6]) repeated 10K times
    n = 6
    l = list(range(1, n+1))
    self.__subtest(n-1, [99] + (l * 10000), n=len(l)*10000 + 1)

  @timeout_decorator.timeout(0.550)
  def test_large_2(self):
    # chaotic sequence of 200K values from [100K..120K], then 200K values from [0..100K]
    self.assertTrue(solution(self.__random_list(100000, 120000, 200000) + self.__random_list(0, 100000, 200000)) > -1)

  @timeout_decorator.timeout(0.550)
  def test_large_3(self):
    # chaotic sequence of 200K values from [1..200K]
    self.assertTrue(solution(self.__random_list(1, 200000, 200000)) > -1)

  # Util

  def __subtest(self, expected, array, **kwargs):
    with self.subTest(**kwargs):
      self.assertEqual(expected, solution(array))

  def __test_sequence(self, n, ascending=True):
    if ascending:
      self.__subtest(n - 1, range(n), n=n, ascending=ascending)
    else:
      self.__subtest(0, range(n - 1, -1, -1), n=n, ascending=ascending)

  @staticmethod
  def __random_list(low, high, size):
    return list(np.random.random_integers(low, high, size))


if __name__ == '__main__':
  unittest.main()
