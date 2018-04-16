#!/usr/bin/env python3

import unittest

import numpy as np
import timeout_decorator

from challenges.codility.lessons.q023.dominator_v001 import *

MAX_N = 100000
MIN_ELEMENT = -2147483648
MAX_ELEMENT = 2147483647

class DominatorTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertIn(solution([3, 4, 3, 2, 3, -1, 3, 3]), [0, 2, 4, 6, 7])

  # Correctness

  def test_small_nondominator(self):
    # all different and all the same elements
    self.assertIn(solution([3, 4, 5, 2, 1, 0, 6, 7]), [-1])
    self.__test([3] * 8, 3)

  def test_small_half_positions(self):
    # half elements the same, and half + 1 elements the same
    n = 20
    self.__test(n * [3] + [2] * (n + 1), 2)
    self.__test((n + 1) * [3] + [2] * n, 3)

  def test_small(self):
    # all different and all the same elements
    self.__test([3, 4, 3], 3)
    self.assertIn(solution([3, 4, 3, 4, 4, 3]), [-1])

  def test_small_pyramid(self):
    # decreasing and plateau, small
    self.__test_pyramid(100)

  def test_extreme_empty_and_single_item(self):
    # empty and single element arrays
    self.assertEqual(-1, solution([]))
    self.assertEqual(0, solution([7]))

  def test_extreme_half1(self):
    # array with exactly N/2 values 1, N even + [0,0,1,1,1]
    N = 58
    n = N // 2
    self.__test(n*[1] + n*[0] + [0, 0, 1, 1, 1], 1)
    self.__test(n*[0] + n*[1] + [0, 0, 1, 1, 1], 1)

  def test_extreme_half2(self):
    # array with exactly floor(N/2) values 1, N odd + [0,0,1,1,1]
    N = 59
    n = N // 2
    self.assertEqual(-1, solution(n*[1] + (n + 1)*[0] + [0, 0, 1, 1, 1]))
    self.assertEqual(-1, solution((n + 1)*[0] + n*[1] + [0, 0, 1, 1, 1]))

  def test_extreme_half3(self):
    # array with exactly ceil(N/2) values 1 + [0,0,1,1,1]
    N = 59
    n = N // 2 + 1
    self.__test(n*[1] + (n - 1)*[0] + [0, 0, 1, 1, 1], 1)
    self.__test((n - 1)*[0] + n*[1] + [0, 0, 1, 1, 1], 1)

  # Performance

  @timeout_decorator.timeout(0.050)
  def test_medium_pyramid(self):
    # decreasing and plateau, medium
    self.__test_pyramid(5000)

  @timeout_decorator.timeout(0.100)
  def test_large_pyramid(self):
    # decreasing and plateau, large
    self.__test_pyramid(MAX_N)

  @timeout_decorator.timeout(0.050)
  def test_medium_random(self):
    # random test with dominator, N = 10,000
    self.__test(*self.__get_random_input(10000))


  @timeout_decorator.timeout(0.150)
  def test_large_random(self):
    # random test with dominator, N = 100,000
    self.__test(*self.__get_random_input(100000))

  # Util

  def __test(self, array, leader):
    s = solution(array)
    if s == -1:
      self.assertTrue(leader == -1)
    else:
      self.assertTrue(array[s] == leader)

  def __test_pyramid(self, N):
    # decreasing and plateau
    n = N // 2
    self.__test(list(range(n)) + (n + 1) * [n + 1], n + 1)

  @staticmethod
  def __get_random_input(n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT):
    l = list(np.random.random_integers(min_value, max_value, n // 2))
    leader = max(l) + 1
    l = l + [leader]*(n // 2 + 1)
    np.random.shuffle(l)
    return l, leader


if __name__ == '__main__':
  unittest.main()
