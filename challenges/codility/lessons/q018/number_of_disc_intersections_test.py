#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q018.number_of_disc_intersections_v001 import *

MAX_N = 100000
MIN_ELEMENT = 0
MAX_ELEMENT = 2147483647


class NumberOfDiscIntersectionsTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(11, solution([1, 5, 2, 1, 4, 0]))

  # Correctness

  def test_simple1(self):
    self.assertEqual(1, solution([1, 0]))

  def test_simple2(self):
    self.assertEqual(0, solution([0, 0]))
    self.assertEqual(1, solution([0, 1]))

  def test_simple3(self):
    self.assertEqual(3, solution([0, 1, 2]))

  def test_extreme_small (self):
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([10]))

  def test_small1(self):
    self.assertEqual(6, solution([1, 2, 3, 4]))

  def test_small2(self):
    self.assertEqual(10, solution([1, 2, 3, 4, 5]))

  def test_small3(self):
    self.assertEqual(10, solution([1, 2, 1, 0, 0, 6]))

  def test_overflow(self):
    # arithmetic overflow tests
    self.assertEqual(-1, solution(list(range(MAX_N))))
    self.assertEqual(-1, solution(list(range(MAX_N // 2))))

  # Performance

  @timeout_decorator.timeout(0.075)
  def test_medium1(self):
    self.assertEqual(300, solution(list(range(25))))

  @timeout_decorator.timeout(0.075)
  def test_medium2(self):
    self.assertEqual(990, solution(list(range(45))))

  @timeout_decorator.timeout(0.075)
  def test_medium3(self):
    self.assertEqual(1485, solution(list(range(55))))

  @timeout_decorator.timeout(0.075)
  def test_medium4(self):
    self.assertEqual(1770, solution(list(range(60))))

  @timeout_decorator.timeout(0.175)
  def test_10M_intersections(self):
    # 10.000.000 intersections
    self.assertEqual(9997156, solution(list(range(4472))))
    self.assertEqual(-1, solution(list(range(4473))))

  @timeout_decorator.timeout(0.175)
  def test_big1(self):
    self.assertEqual(-1, solution(list(range(5000))))
    self.assertEqual(-1, solution(list(range(10000))))

  @timeout_decorator.timeout(0.675)
  def test_big2(self):
    self.assertEqual(-1, solution(list(range(50000))))
    self.assertEqual(-1, solution(list(range(100000))))

  @timeout_decorator.timeout(0.575)
  def test_big3(self):
    self.assertEqual(0, solution([0]*50000))
    self.assertEqual(99997, solution([1]*50000))


if __name__ == '__main__':
  unittest.main()
