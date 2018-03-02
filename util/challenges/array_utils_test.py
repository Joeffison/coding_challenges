#!/usr/bin/env python3

import random
import unittest

from util.challenges.array_utils import get_missing_value


class GetMissingValueTestCase(unittest.TestCase):

  @staticmethod
  def __get_random_input_and_solution(n):
    array = list(range(1, n + 2))
    solution = random.choice(array)
    array.pop(solution - 1)
    random.shuffle(array)
    return solution, array

  def test_description_examples(self):
    self.assertEqual(get_missing_value([2, 3, 1, 5]), 4)

  def test_empty_and_single(self):
    self.assertEqual(get_missing_value([]), 1)
    self.assertEqual(get_missing_value([2]), 1)

  def test_missing_first_or_last(self):
    self.assertEqual(get_missing_value([2, 3, 7, 8, 4, 5, 6, 9, 10]), 1)
    self.assertEqual(get_missing_value([2, 3, 7, 8, 4, 5, 6, 9, 1]), 10)

  def test_single(self):
    self.assertEqual(get_missing_value([1]), 2)

  def test_double(self):
    self.assertEqual(get_missing_value([2, 1]), 3)

  def test_simple(self):
    self.assertEqual(get_missing_value([1, 2, 3]), 4)

  def test_medium1(self):
    expected, array = self.__get_random_input_and_solution(10000)
    self.assertEqual(get_missing_value(array), expected)

  def test_medium2(self):
    expected, array = self.__get_random_input_and_solution(10000)
    self.assertEqual(get_missing_value(array), expected)

  def test_large_range(self):
    n = 100000

    expected, array = self.__get_random_input_and_solution(n)
    with self.subTest(solution=expected, n=n):
      self.assertEqual(get_missing_value(array), expected)

    expected, array = self.__get_random_input_and_solution(n)
    with self.subTest(solution=expected, n=n):
      self.assertEqual(get_missing_value(array), expected)

    expected, array = self.__get_random_input_and_solution(n)
    with self.subTest(solution=expected, n=n):
      self.assertEqual(get_missing_value(array), expected)

  def test_large1(self):
    expected, array = self.__get_random_input_and_solution(100000)
    self.assertEqual(get_missing_value(array), expected)

  def test_large2(self):
    expected, array = self.__get_random_input_and_solution(100000)
    self.assertEqual(get_missing_value(array), expected)

if __name__ == '__main__':
  unittest.main()
