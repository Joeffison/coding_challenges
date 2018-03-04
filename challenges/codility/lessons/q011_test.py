#!/usr/bin/env python3

import unittest

import timeout_decorator
from challenges.codility.lessons.q011_v001 import *

MIN_ELEMENT = 0
MAX_ELEMENT = 2000000000

class Codility11TestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(3, solution(6, 11, 2))

  # Correctness

  def test_simple(self):
    self.assertEqual(20, solution(11, 345, 17))

  def test_minimal(self):
    self.assertEqual(1, solution(0, 0, 11))
    self.assertEqual(1, solution(0, 1, 11))
    self.assertEqual(0, solution(1, 1, 11))

  def test_extreme_if_empty(self):
    a, b = 10, 10
    ks = [5, 7, 20]
    solutions = [1 if a % k == 0 else 0 for k in ks]

    for i in range(len(ks)):
      with self.subTest(a=a, b=b, k=ks[i]):
        self.assertEqual(solutions[i], solution(a, b, ks[i]))

  def test_extreme_endpoints(self):
    for i in range(6):
      a, b, k = MIN_ELEMENT, MAX_ELEMENT, MAX_ELEMENT
      with self.subTest(a=a, b=b, k=k):
        self.assertEqual(2, solution(a, b, k))

  # Performance

  @timeout_decorator.timeout(0.036)
  def test_big_values(self):
    self.assertEqual(61499951, solution(100, 123000000, 2))

  @timeout_decorator.timeout(0.036)
  def test_big_values2(self):
    self.assertEqual(12300, solution(101, 123000000, 10000))

  @timeout_decorator.timeout(0.036)
  def test_big_values3(self):
    self.assertEqual(MAX_ELEMENT + 1, solution(0, MAX_ELEMENT, 1))
    self.assertEqual(2, solution(0, MAX_ELEMENT, MAX_ELEMENT))

  @timeout_decorator.timeout(0.036)
  def test_big_values4(self):
    # A, B, K in {1,MAXINT}
    self.assertEqual(1, solution(1, 1, 1))
    self.assertEqual(0, solution(1, 1, MAX_ELEMENT))
    self.assertEqual(MAX_ELEMENT, solution(1, MAX_ELEMENT, 1))
    self.assertEqual(1, solution(1, MAX_ELEMENT, MAX_ELEMENT))
    self.assertEqual(1, solution(MAX_ELEMENT, MAX_ELEMENT, 1))
    self.assertEqual(1, solution(MAX_ELEMENT, MAX_ELEMENT, MAX_ELEMENT))

if __name__ == '__main__':
  unittest.main()
