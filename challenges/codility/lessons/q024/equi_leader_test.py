#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q024.equi_leader_v001 import *

MAX_N = 100000
MIN_ELEMENT = -1000000000
MAX_ELEMENT = 1000000000

class DominatorTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(2, solution([4, 3, 4, 4, 4, 2]))

  # Correctness

  def test_single(self):
    self.assertEqual(0, solution([0]))
    self.assertEqual(0, solution([1]))
    self.assertEqual(0, solution([2]))

  def test_double(self):
    self.assertEqual(1, solution([0, 0]))
    self.assertEqual(1, solution([1, 1]))
    self.assertEqual(0, solution([1, 0]))

  def test_simple(self):
    self.assertEqual(0, solution([0, 1, 0]))
    self.assertEqual(2, solution([0, 1, 0, 0]))
    self.assertEqual(1, solution([1, 0, 0, 0]))

  def test_small_random(self):
    # small random test with two values, length = ~100
    pass

  def test_small(self):
    # random + 200 * [MIN_INT] + random ,length = ~300
    pass

  # Performance

  def test_large_random(self):
    # large random test with two values, length = ~50,000
    pass

  def test_large(self):
    # random(0,1) + 50000 * [0] + random(0, 1), length = ~100,000
    pass

  @timeout_decorator.timeout(0.550)
  def test_large_range(self):
    # 1, 2, ..., N, length = ~100,000
    self.assertEqual(0, solution(list(range(1, MAX_N + 1))))
    self.assertEqual(0, solution(list(range(0, MAX_N))))

  @timeout_decorator.timeout(0.550)
  def test_extreme_large(self):
    # all the same values
    n = MAX_N
    self.assertEqual(n - 1, solution([5]*n))


if __name__ == '__main__':
  unittest.main()
