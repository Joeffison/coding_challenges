#!/usr/bin/env python3

import unittest

import timeout_decorator
import numpy as np

from challenges.codility.lessons.q021.fish_v002 import *

MAX_N = 100000
MIN_ELEMENT = 0
MAX_ELEMENT = 1000000000


class FishTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(2, solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))

  # Correctness

  def test_extreme_small(self):
    self.assertEqual(1, solution([4], [0]))
    self.assertEqual(1, solution([4], [1]))
    self.assertEqual(1, solution([0], [0]))
    self.assertEqual(1, solution([0], [1]))
    self.assertEqual(1, solution([1], [0]))
    self.assertEqual(1, solution([1], [1]))
    self.assertEqual(1, solution([77], [0]))

  def test_simple1(self):
    self.assertEqual(1, solution([4, 2, 3], [1, 0, 0]))

  def test_simple2(self):
    self.assertEqual(1, solution([4, 5], [1, 0]))
    self.assertEqual(2, solution([4, 5], [0, 1]))

  def test_small_random(self):
    # small random test, N = ~100
    self.__test_random(100)

  # Performance

  @timeout_decorator.timeout(0.084)
  def test_medium_random(self):
    # small medium test, N = ~5,000
    self.__test_random(5000)

  @timeout_decorator.timeout(0.940)
  def test_large_random(self):
    # large random test, N = ~100,000
    self.__test_random(MAX_N)

  @timeout_decorator.timeout(0.084)
  def test_extreme_range1(self):
    # all except one fish flowing in the same direction
    n = 5000
    sizes = list(self.__get_random_array(n, MIN_ELEMENT + 1, MAX_ELEMENT - 1))
    fish = [1] * n + [0]
    self.assertEqual(1, solution(sizes + [MAX_ELEMENT], fish))
    self.assertEqual(n, solution(sizes + [MIN_ELEMENT], fish))

  @timeout_decorator.timeout(0.084)
  def test_extreme_range2(self):
    # all fish flowing in the same direction
    n = 5000
    sizes = list(self.__get_random_array(n, MIN_ELEMENT + 1, MAX_ELEMENT - 1))
    self.assertEqual(n, solution(sizes, [0] * n))
    self.assertEqual(n, solution(sizes, [1] * n))

  # Util

  @staticmethod
  def __brute_solution(sizes, directions):
    alive = 0
    upstream = []
    for i in range(len(directions)):
      if directions[i] == 0:
        alive += 1
        while upstream:
          if sizes[upstream[-1]] > sizes[i]:
            alive -= 1
            break
          else:
            upstream.pop()
      else:
        upstream.append(i)

    return alive + len(upstream)

  def __test(self, sizes, directions):
    with self.subTest(n=len(directions)):
      self.assertEqual(self.__brute_solution(sizes, directions), solution(sizes, directions))

  @staticmethod
  def __get_random_array(n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT):
    return np.random.random_integers(min_value, max_value, n)

  def __test_random(self, n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT):
    self.__test(self.__get_random_array(n, min_value, max_value), np.random.random_integers(0, 1, n))

if __name__ == '__main__':
  unittest.main()
