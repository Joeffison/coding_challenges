#!/usr/bin/env python3

import unittest

import timeout_decorator
import numpy as np

from challenges.codility.lessons.q026.max_slice_sum_v001 import *
from util.challenges.array_challenges import sum_first_n_natural_numbers

MAX_N = 1000000
MIN_ELEMENT = -1000000
MAX_ELEMENT = 1000000

class MaxSliceSumTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(5, solution([3, 2, -6, 4, 0]))

  # Correctness

  def test_one_element(self):
    self.assertEqual(-10, solution([-10]))
    self.assertEqual(0, solution([0]))
    self.assertEqual(10, solution([10]))

  def test_two_elements(self):
    self.assertEqual(-2, solution([-2, -3]))
    self.assertEqual(0, solution([0, -1]))
    self.assertEqual(0, solution([-1, 0]))
    self.__test_random_positive(2, 6)

  def test_three_elements(self):
    self.assertEqual(-2, solution([-4, -2, -3]))
    self.__test_random_positive(3, 26)

  def test_simple(self):
    self.assertEqual(3, solution([0, 1, 2]))

  def test_extreme_minimum(self):
    self.assertEqual(MIN_ELEMENT, solution([MIN_ELEMENT]))

  def test_fifty_random(self):
    self.__test_random_positive(50)

  def test_neg_const(self):
    self.assertEqual(-11, solution([-11]))

  def test_pos_const(self):
    self.assertEqual(11, solution([11]))

  # Performance

  @timeout_decorator.timeout(0.050)
  def test_high_low_1Kgarbage(self):
    self.__test_random_positive(1000)

  @timeout_decorator.timeout(3.550)
  def test_1Kgarbage_high_low(self):
    self.__test_random_positive(MAX_N)

  @timeout_decorator.timeout(0.550)
  def test_growing_saw(self):
    l = []
    array = []
    n = 25
    for i in range(n):
      l.append(i)
      array += l
    self.assertEqual(sum([sum_first_n_natural_numbers(i) for i in range(n)]), solution(array))


  @timeout_decorator.timeout(0.550)
  def test_blocks(self):
    block = [0, 1, 2, 3, 4]
    n = 10
    self.assertEqual(sum(block)*n, solution(block*n))

  @timeout_decorator.timeout(2.550)
  def test_growing_negative(self):
    self.assertEqual(-1, solution(range(-1, MIN_ELEMENT, -1)))

  # Utils

  def __test_random_positive(self, size, iterations=1):
    for i in range(iterations):
      with self.subTest(i=i):
        l = list(np.random.random_integers(0, MAX_ELEMENT, size))
        self.assertEqual(sum(l), solution(l))


if __name__ == '__main__':
  unittest.main()
