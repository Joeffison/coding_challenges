#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q014.min_avg_two_slice_v001 import *

MAX_N = 100000
MIN_ELEMENT = -10000
MAX_ELEMENT = 10000


class MinAvgTwoSliceTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(1, solution([4, 2, 2, 5, 1, 5, 8]))

  # Correctness

  def test_double_quadruple(self):
    self.assertEqual(0, solution([8, 2]))
    self.assertEqual(0, solution([-1, 1, 2, 3]))
    self.assertEqual(2, solution([2, 3, -1, 1]))
    self.assertEqual(1, solution([7, 2, 4, 1]))

  def test_simple1(self):
    self.assertEqual(1, solution([9, 2, 4, 1]))
    self.assertEqual(0, solution([2, 3, 1]))

  def test_simple2(self):
    self.assertEqual(0, solution([5, 9, 1]))

  def test_small_random(self):
    self.__test_random(100)

  def test_medium_range(self):
    array = list(range(0, 200, 4)) + list(range(400, 300, -2))
    self.assertEqual(0, solution(array))

    array = list(range(100, 300, 4)) + list(range(400, 300, -2))
    self.assertEqual(0, solution(array))

    array = list(range(0, 90, 3)) + list(range(650, 300, -5))
    self.assertEqual(0, solution(array))

  # Performance

  def test_medium_random(self):
    self.__test_random(700)

  def test_large_ones(self):
    self.__test_random(MAX_N, -1, 1)
    self.__test_random(MAX_N, -1, 1)

  def test_large_random(self):
    self.__test_random(MAX_N)

  def test_extreme_values(self):
    self.assertEqual(0, solution([MAX_ELEMENT]*MAX_N))
    self.assertEqual(0, solution([MIN_ELEMENT]*MAX_N))

    array = [MIN_ELEMENT]*(MAX_N//2) + [MAX_ELEMENT]*(MAX_N//2)
    random.shuffle(array)
    pos = array.index(MIN_ELEMENT)
    self.assertEqual(self.__brute_solution(array), solution(array))

  def test_large_sequence(self):
    self.assertEqual(0, solution(list(range(MAX_N))))

  # Utils

  @staticmethod
  def __brute_solution(array):
    min_avg = (array[0] + array[1]) / 2.0
    min_pos = 0

    for i in range(len(array)-1):
      for j in range(i + 2, len(array) + 1):
        current_avg = sum(array[i:j])/(j-i)

        if current_avg < min_avg:
          min_avg = current_avg
          min_pos = i

    return min_pos

  def __test_random(self, n, min=MIN_ELEMENT, max=MAX_ELEMENT):
    array = list(np.random.random_integers(min, max, n))

    with self.subTest(n=n):
      self.assertEqual(self.__brute_solution(array), solution(array))

if __name__ == '__main__':
  unittest.main()
