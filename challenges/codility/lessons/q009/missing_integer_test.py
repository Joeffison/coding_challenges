#!/usr/bin/env python3

import random
import unittest

import numpy as np
import timeout_decorator

from challenges.codility.lessons.q009.missing_integer_v002 import *

MIN_RESULT = 1
MIN_ELEMENT = -1000000
MAX_ELEMENT = 1000000


class MissingIntegerTestCase(unittest.TestCase):

  def test_example1(self):
    self.assertEqual(5, solution([1, 3, 6, 4, 1, 2]))

  def test_example2(self):
    self.assertEqual(4, solution([1, 2, 3]))

  def test_example3(self):
    self.assertEqual(MIN_RESULT, solution([-1, -3]))

  # Correctness

  def test_single(self):
    self.assertEqual(MIN_RESULT, solution([-1]))
    self.assertEqual(1, solution([0]))
    self.assertEqual(2, solution([1]))
    self.assertEqual(1, solution([2]))

  def test_simple(self):
    self.assertEqual(1, solution([2, 3, 4]))
    self.assertEqual(4, solution([1, 2, 3]))
    self.assertEqual(1, solution([2, 3, 4]))

  def test_extreme_min_max_value(self):
    self.assertEqual(1, solution([MIN_ELEMENT]))
    self.assertEqual(1, solution([MAX_ELEMENT]))

  def test_positive_only(self):
    array = list(range(0, 101))
    random.shuffle(array)
    self.assertEqual(101, solution(array))

    array = list(range(102, 201))
    random.shuffle(array)
    self.assertEqual(MIN_RESULT, solution(array))

  def test_only_negatives(self):
    """
    Tests that lists (of length: |n| - 1)
    containing numbers between -1 and n
    return MIN_RESULT
    """
    self.assertEqual(MIN_RESULT, solution(self.__negative_list(-100)))

  # Performance

  def test_medium(self):
    array = np.random.random_integers(MIN_ELEMENT, MAX_ELEMENT, 10005)
    self.__test_timeout_050(self.__brute_solution(array), array)

    array = np.random.random_integers(MIN_ELEMENT, MAX_ELEMENT, 10005)
    self.__test_timeout_050(self.__brute_solution(array), array)

    array = np.random.random_integers(MIN_ELEMENT, MAX_ELEMENT, 10005)
    self.__test_timeout_050(self.__brute_solution(array), array)

  def test_large_1(self):
    array = list(np.random.random_integers(1, MAX_ELEMENT, 100)) + list(range(1, 40001))
    self.__test_timeout_175(self.__brute_solution(array), array)

  def test_large_2(self):
    array = list(range(1, 100001))
    random.shuffle(array)
    self.__test_timeout_275(len(array) + 1, array)

    array = list(range(1, 100001))
    random.shuffle(array)
    self.__test_timeout_275(len(array) + 1, array)

  def test_large_3(self):
    array = list(np.random.random_integers(MIN_ELEMENT, MAX_ELEMENT, 100)) + random.choices([-1, 1, 2, 3], k=100000)
    # self.assertEqual(self.__brute_solution(array), solution(array))
    self.__test_timeout_175(self.__brute_solution(array), array)

  # Util

  @staticmethod
  def __brute_solution(array):
    array.sort()
    for i in range(1, len(array) + 1):
      if i not in array:
        return i
    return len(array) + 1

  @timeout_decorator.timeout(0.275)
  def __test_timeout_275(self, expected_result, array):
    self.assertEqual(expected_result, solution(array))

  @timeout_decorator.timeout(0.175)
  def __test_timeout_175(self, expected_result, array):
    self.assertEqual(expected_result, solution(array))

  @timeout_decorator.timeout(0.065)
  def __test_timeout_050(self, expected_result, array):
    self.assertEqual(expected_result, solution(array))

  @staticmethod
  def __negative_list(end_value, ordered=False, start_value=-1):
    """
    Creates a list of negative values using the given range.

    :param end_value: Smallest value (inclusive)
    :param ordered: If false, array is shuffled
    :param start_value: Biggest value (inclusive). Default is -1.
    :return: List of negative values
    """
    response = list(range(start_value, end_value - 1, -1))

    if not ordered:
      random.shuffle(response)
    return response

if __name__ == '__main__':
  unittest.main()
