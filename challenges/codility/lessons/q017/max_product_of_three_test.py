#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q017.max_product_of_three_v001 import *

MAX_N = 100000
MIN_ELEMENT = -1000
MAX_ELEMENT = 1000


class MaxProductOfThreeTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(60, solution([-3, 1, 2, -2, 5, 6]))

  # Correctness

  def test_one_triple(self):
    self.assertEqual(-6, solution([-1, 2, 3]))
    self.assertEqual(0, solution([8, 0, 3]))
    self.assertEqual(30, solution([5, 2, 3]))

  def test_simple1(self):
    self.__test([-10, -3, -6, 6, 1, 0])
    self.__test_sequence(10)
    self.__test(list(range(3, 99, 3)))
    self.__test(list(range(34, 100, 2)))

  def test_simple2(self):
    self.__test_sequence(100)
    self.__test([-4, -3, -5, -1, -2])
    self.__test(list(list(range(MIN_ELEMENT, 0, 100))))

  def test_small_random(self):
    self.__test_random(100)

  # Performance

  def test_medium_range(self):
    self.__test_sequence(abs(MIN_ELEMENT) + abs(MAX_ELEMENT), MIN_ELEMENT, False)

  def test_medium_random(self):
    self.__test_random(10000)

  def test_large_random(self):
    self.__test_random(100000)

  def test_large_range(self):
    # 2000 * (-10..10) + [-1000, 500, -1]
    self.__test((2000 * list(range(-10, 11))) + [-1000, 500, -1])

  def test_extreme_large(self):
    #(-2, .., -2, 1, .., 1) and (MAX_INT)..(MAX_INT), length = ~100, 000
    n = 100000
    l = ([-2] * (n // 2)) + ([1] * (n // 2))
    self.assertEqual(4, solution(l))

    self.assertEqual(pow(MAX_ELEMENT, 3), solution([MAX_ELEMENT] * n))

  # Utils

  @staticmethod
  def __brute_solution(array):
    array = list(array).copy()

    a = max(array)
    array.remove(a)
    b = max(array)
    array.remove(b)
    c = max(array)
    array.remove(c)

    if len(array) > 1:
      d = min(array)
      array.remove(d)
      e = min(array)
      return max(a * b * c, a * d * e)
    return a * b * c

  def __test(self, array):
    with self.subTest(n=len(array)):
      self.assertEqual(self.__brute_solution(array), solution(array))

  def __test_random(self, n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT):
    self.__test(np.random.random_integers(min_value, max_value, n))

  def __test_sequence(self, n=100, min_value=0, shuffled=True):
    l = list(range(min_value, min_value + n))

    if shuffled:
      random.shuffle(l)

    self.__test(l)

if __name__ == '__main__':
  unittest.main()
