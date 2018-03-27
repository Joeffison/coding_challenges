#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q015.triangle_v001 import *

MAX_N = 100000
MIN_ELEMENT = -2147483648
MAX_ELEMENT = 2147483647


class TriangleTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(1, solution([10, 2, 5, 1, 8, 20]))
    self.assertEqual(0, solution([10, 50, 5, 1]))

  # Correctness

  def test_extreme_empty(self):
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([]))
    self.assertEqual(0, solution([]))

  def test_extreme_single(self):
    self.assertEqual(0, solution([50]))
    self.assertEqual(0, solution([MIN_ELEMENT]))
    self.assertEqual(0, solution([-1]))
    self.assertEqual(0, solution([0]))
    self.assertEqual(0, solution([2]))
    self.assertEqual(0, solution([4]))

  def test_extreme_two_elems(self):
    self.assertEqual(0, solution([MIN_ELEMENT, MAX_ELEMENT]))
    self.assertEqual(0, solution([MIN_ELEMENT, 0]))
    self.assertEqual(0, solution([-1, -1]))
    self.assertEqual(0, solution([0, 2]))
    self.assertEqual(0, solution([4, 4]))
    self.assertEqual(0, solution([4, 2]))

  def test_extreme_negative1(self):
    # three equal negative numbers
    self.assertEqual(0, solution([-1] * 3))
    self.assertEqual(0, solution([MIN_ELEMENT] * 3))
    self.assertEqual(0, solution([-10] * 3))
    self.assertEqual(0, solution([-50] * 3))
    self.assertEqual(0, solution([-15] * 3))
    self.assertEqual(0, solution([-12] * 3))

  def test_extreme_arith_overflow1(self):
    # overflow test, 3 MAXINTs
    self.assertEqual(1, solution([MAX_ELEMENT] * 3))
    self.assertEqual(1, solution([MAX_ELEMENT] * 3 + [0]))
    self.assertEqual(1, solution([0] + [MAX_ELEMENT] * 3))
    self.assertEqual(1, solution([0, 2] + [MAX_ELEMENT] * 3))
    self.assertEqual(1, solution([MAX_ELEMENT] * 3 + [0, 2]))
    self.assertEqual(1, solution([MAX_ELEMENT] * 3 + [-1]))

  def test_extreme_arith_overflow2(self):
    # overflow test, 10 and 2 MININTs
    self.assertEqual(0, solution([MIN_ELEMENT] * 10))
    self.assertEqual(0, solution([MIN_ELEMENT] * 2))
    self.assertEqual(0, solution([MIN_ELEMENT] * 2 + [10]))
    self.assertEqual(0, solution([10] + [MIN_ELEMENT] * 2))
    self.assertEqual(0, solution([10, 10] + [MIN_ELEMENT] * 2))
    self.assertEqual(0, solution([MIN_ELEMENT] * 2 + [10, 10]))

  def test_extreme_arith_overflow3(self):
    # overflow test, 0 and 2 MAXINTs
    self.assertEqual(0, solution([MAX_ELEMENT] * 0))
    self.assertEqual(0, solution([MAX_ELEMENT] * 2))
    self.assertEqual(0, solution([MAX_ELEMENT] * 2 + [0]))
    self.assertEqual(0, solution([0] + [MAX_ELEMENT] * 2))
    self.assertEqual(1, solution([0, 2] + [MAX_ELEMENT] * 2))
    self.assertEqual(1, solution([MAX_ELEMENT] * 2 + [0, 2]))

  def test_medium1(self):
    # chaotic sequence of values from [0..100K], length=30
    for i in range(6):
      self.__test_random(30, 0, 100000)

  def test_medium2(self):
    # chaotic sequence of values from [0..1K], length=50
    for i in range(6):
      self.__test_random(50, 0, 1000)

  def test_medium3(self):
    # chaotic sequence of values from [0..1K], length=100
    for i in range(6):
      self.__test_random(100, 0, 1000)

  # Performance

  def test_large1(self):
    # chaotic sequence with values from [0..100K], length=10K
    for i in range(6):
      self.__test_random(10000, 0, 100000)

  def test_large2(self):
    # 1 followed by an ascending sequence of ~50K elements from [0..100K], length=~50K
    for i in range(6):
      self.__test([1] + self.__create_random_array(50000, 0, 100000, False))

  def test_large_random(self):
    # chaotic sequence of values from [0..1M], length=100K
    for i in range(6):
      self.__test_random(100000, 0, 1000000)

  def test_large_negative(self):
    # chaotic sequence of negative values from [-1M..-1], length=100K
    for i in range(6):
      self.assertEqual(0, solution(self.__create_random_array(100000, -1000000, -1)))

  def test_large_negative2(self):
    # chaotic sequence of negative values from [-10.. - 1], length = 100K
    for i in range(6):
      self.assertEqual(0, solution(self.__create_random_array(100000, -10, -1)))

  def test_large_negative3(self):
    # sequence of -1 value, length=100K
    for i in range(6):
      self.assertEqual(0, solution([-1] * 100000))

  # Utils

  @staticmethod
  def __brute_solution(array):
    if len(array) > 2:
      # The following lines are used to reduce the input
      from collections import Counter
      counts = Counter(array)
      array = [item for item in array if counts[item] < 4] + \
              ([i for i in set([item for item in array if counts[item] > 3])] * 3)

      for i in range(len(array) - 2):
        if(array[i]) < 0: continue

        for j in range(i + 1, len(array) - 1):
          if (array[j]) < 0: continue

          for k in range(j + 1, len(array)):
            if (array[k]) > -1 and (array[i] + array[j] > array[k]) and \
              (array[i] + array[k] > array[j]) and (array[k] + array[j] > array[i]):
              return 1

    return 0

  def __test(self, array):
    with self.subTest(n=len(array)):
      self.assertEqual(self.__brute_solution(array), solution(array))

  @staticmethod
  def __create_random_array(n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT, shuffled=True):
    array = np.random.random_integers(min_value, max_value, n)

    if not shuffled:
      array = list(array)
      array.sort()

    return array

  def __test_random(self, n, min_value=MIN_ELEMENT, max_value=MAX_ELEMENT):
    self.__test(self.__create_random_array(n, min_value, max_value))

  def __test_sequence(self, n=100, min_value=0, shuffled=True):
    l = list(range(min_value, min_value + n))

    if shuffled:
      random.shuffle(l)

    self.__test(l)

if __name__ == '__main__':
  unittest.main()
