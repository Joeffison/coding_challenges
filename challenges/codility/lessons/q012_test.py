#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q012_v001 import *

MAX_N = 100000

class Codility12TestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(5, solution([0, 1, 0, 1, 1]))

  # Correctness

  def test_single(self):
    self.assertEqual(0, solution([0]))
    self.assertEqual(0, solution([1]))

  def test_double(self):
    self.assertEqual(0, solution([0, 0]))
    self.assertEqual(1, solution([0, 1]))
    self.assertEqual(0, solution([1, 1]))
    self.assertEqual(0, solution([1, 0]))

  def test_small_simple(self):
    self.assertEqual(3, solution([0, 1, 1, 1]))

  def test_small_random1(self):
    self.__test_random(100)

  def test_small_random2(self):
    self.__test_random(1000)

  # Performance
  def test_medium_random(self):
    self.__test_random(MAX_N)

  def test_large_random(self):
    self.__test_random(MAX_N)

  def test_large_big_answer(self):
    self.__test_random(MAX_N)
    self.__test_random(MAX_N)

  def test_large_alternate(self):
    array = [0, 1] * (MAX_N // 2)
    self.assertEqual(self.__brute_solution(array), solution(array))

    array = [1, 0] * (MAX_N // 2)
    self.assertEqual(self.__brute_solution(array), solution(array))

  def test_large_extreme(self):
    self.assertEqual(0, solution([0] * MAX_N))
    self.assertEqual(0, solution([1] * MAX_N))
    self.assertEqual(-1, solution(([0] * (MAX_N // 2)) + ([1] * (MAX_N // 2))))
    self.assertEqual(0, solution(([1] * (MAX_N // 2)) + ([0] * (MAX_N // 2))))

  # Utils

  @staticmethod
  def __brute_solution(array):
    result = 0
    saw_one = False
    for i in range(len(array) - 1):
      saw_one |= array[i]
      if array[i] == 0:
        result += sum(array[i + 1:])
        if result > 1000000000:
          return -1
    return result

  def __test_random(self, n):
    array = list(np.random.random_integers(0, 1, n))
    random.shuffle(array)

    with self.subTest(n=n):
      self.assertEqual(self.__brute_solution(array), solution(array))

if __name__ == '__main__':
  unittest.main()
