#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q027.max_double_slice_sum_v001 import *
from util.challenges.array_challenges import sum_first_n_natural_numbers

MAX_N = 100000
MIN_ELEMENT = -10000
MAX_ELEMENT = 10000

class MaxDoubleSliceSumTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(17, solution([3, 2, 6, -1, 4, 5, -1, 2]))

  # Correctness

  def test_simple1(self):
    self.__sub_test(0, [0, 1, 2])
    self.__sub_test(1, [MIN_ELEMENT, 0, 1, 2])
    self.__sub_test(2, [0, 1, 2, MAX_ELEMENT])

  def test_simple2(self):
    self.__sub_test(0, [MIN_ELEMENT, MIN_ELEMENT, MIN_ELEMENT, MIN_ELEMENT])
    self.__sub_test(MAX_ELEMENT, [0, MAX_ELEMENT, 1, 2])

  def test_simple3(self):
    self.__sub_test(0, [0, 1, 2])

  def test_negative(self):
    self.__sub_test(0, range(-1, MIN_ELEMENT - 1, -1))

  def test_positive(self):
    self.__sub_test(sum_first_n_natural_numbers(MAX_ELEMENT - 1) - 1, range(0, MAX_ELEMENT + 1))

  def test_extreme_triplet(self):
    self.__sub_test(0, [1, 2, 3])

  # Performance

  @timeout_decorator.timeout(0.550)
  def test_medium_range(self):
    self.__sub_test(sum_first_n_natural_numbers(1000 - 1), range(-1000, 1001))

  @timeout_decorator.timeout(0.550)
  def test_extreme_maximal(self):
    self.__sub_test(MAX_ELEMENT * (MAX_N - 3), [MAX_ELEMENT] * MAX_N)

  @timeout_decorator.timeout(1.001)
  def test_large_sequence(self):
    self.__sub_test(199996, list(range(5)) * (MAX_N // 5))
    self.__sub_test(2449951, list(range(50)) * (MAX_N // 50))

  # Util

  def __sub_test(self, expected, array, **kwargs):
    if not kwargs:
      kwargs = {'result': expected}

    with self.subTest(**kwargs):
      self.assertEqual(expected, solution(array))


if __name__ == '__main__':
  unittest.main()
