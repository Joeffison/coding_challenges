#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q004.tape_equilibrium_v001 import *

MIN_ELEMENT = -1000
MAX_ELEMENT = 1000


def get_random_list(n, min=MIN_ELEMENT, max=MAX_ELEMENT):
  return list(np.random.random_integers(min, max, (1, n))[0])


def get_random_positive_list(n):
  return get_random_list(n, min=1)


def get_random_negative_list(n):
  return get_random_list(n, max=-1)


def brute_solution(array):
  return min([abs(sum(array[:i]) - sum(array[i:])) for i in range(1, len(array))])


class TapeEquilibriumTestCase(unittest.TestCase):

  # Correctness

  def test_description_examples(self):
    self.assertEqual(solution([3, 1, 2, 4, 3]), 1)

  def test_double(self):
    array = get_random_list(2)
    self.assertEqual(solution(array), brute_solution(array))

  def test_simple_positive(self):
    array = get_random_positive_list(5)
    self.assertEqual(solution(array), brute_solution(array))

  def test_simple_negative(self):
    array = get_random_negative_list(5)
    self.assertEqual(solution(array), brute_solution(array))

  def test_small_random(self):
    array = get_random_negative_list(100)
    self.assertEqual(solution(array), brute_solution(array))

  def test_small_range(self):
    array = get_random_negative_list(1000)
    self.assertEqual(solution(array), brute_solution(array))

  def test_small(self):
    array = get_random_list(1000, -50, 50)
    self.assertEqual(solution(array), brute_solution(array))

  # Performance

  def test_medium_random1(self):
    array = get_random_list(10000, 0, 100)
    self.assertEqual(solution(array), brute_solution(array))

  def test_medium_random2(self):
    array = get_random_list(10000, -1000, 50)
    self.assertEqual(solution(array), brute_solution(array))

  def test_large_ones(self):
    array = get_random_list(100000, -1, 1)
    self.assertEqual(solution(array), brute_solution(array))

  def test_large_random(self):
    array = get_random_list(100000)
    self.assertEqual(solution(array), brute_solution(array))

  def test_large_sequence(self):
    array = list(range(100000))
    self.assertEqual(solution(array), brute_solution(array))

  def test_large_extreme(self):
    array = get_random_list(100000-2) + [MIN_ELEMENT, MAX_ELEMENT]
    random.shuffle(array)
    self.assertEqual(solution(array), brute_solution(array))

if __name__ == '__main__':
  unittest.main()
