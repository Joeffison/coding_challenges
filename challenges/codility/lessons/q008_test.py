#!/usr/bin/env python3

import random
import unittest

from challenges.codility.lessons.q008_v001 import *
from util.array_utils import remove_random

MIN_ELEMENT = 1
MAX_ELEMENT = 100000

class Codility8TestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(6, solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

  # Correctness

  def test_simple(self):
    self.assertEqual(6, solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

  def test_single(self):
    array = [1]
    self.assertEqual(0, solution(0, array))
    self.assertEqual(0, solution(1, array))

  def test_extreme_frog(self):
    # frog never across the river
    for i in range(3):
      array = self.__get_valid_input(20)
      desired_position = remove_random(array, all_occurrences=True)

      with self.subTest(desired_position=desired_position, array=array):
        self.assertEqual(-1, solution(desired_position, array))

  def test_small_random1(self):
    self.__test_random(50)

  def test_small_random2(self):
    self.__test_random(60)

  def test_extreme_leaves(self):
    # all leaves in the same place
    array = list(range(1, 75))
    self.assertEqual(len(array) - 1, solution(len(array), array))

    array = list(range(1, 87))
    self.assertEqual(len(array) - 1, solution(len(array), array))

  # Performance

  def test_medium_random(self):
    self.__test_random(5000)
    self.__test_random(5000)

  def test_medium_range(self):
    # arithmetic sequences, X = 5,000
    self.__test_arithmetic_progression(5000)

  def test_large_random(self):
    # 10 and 100 random permutation, X = ~10,000
    self.__test_random(10000)
    self.__test_random(10000)

  def test_large_permutation(self):
    self.__test_random(30000)
    self.__test_random(30000)

  def test_large_range(self):
    # arithmetic sequences, X = 30,000
    self.__test_arithmetic_progression(30000)

  # Utils

  @staticmethod
  def __brute_solution(desired_position, array):
    # Time Complexity is O(n*m^2), i.e. O(m) for max() and O(n*m) for index() over for loop.
    # No additional space required
    try:
      return max([array.index(i) for i in range(1, desired_position+1)])
    except:
      return -1

  @staticmethod
  def __get_valid_input(n):
    array = list(range(1, n + 1))
    random.shuffle(array)
    return array

  def __test_random(self, desired_position):
    array = self.__get_valid_input(desired_position + ((desired_position * 2) // 3))

    with self.subTest(desired_position=desired_position, n=len(array)):
      self.assertEqual(self.__brute_solution(desired_position, array), solution(desired_position, array))

  def __test_arithmetic_progression(self, desired_position, factor=3):
    n = desired_position + ((desired_position * 2) // 3)

    array = []
    for i in range(1, factor + 1):
      array += list(range(i, n, factor))

    with self.subTest(desired_position=desired_position, n=len(array)):
      self.assertEqual(self.__brute_solution(desired_position, array), solution(desired_position, array))

if __name__ == '__main__':
  unittest.main()
