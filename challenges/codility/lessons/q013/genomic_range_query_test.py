#!/usr/bin/env python3

import random
import unittest

import numpy as np

from challenges.codility.lessons.q013.genomic_range_query_v001 import *
from util.challenges.array_challenges import sum_first_n_natural_numbers

MAX_N = 100000
MAX_M = 50000
classes = ['A', 'C', 'G', 'T']
classes_values = [1, 2, 3, 4]
classes_map = {classes[i]:classes_values[i] for i in range(len(classes))}


class GenomicRangeQueryTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual([2, 4, 1], solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))

  # Correctness

  def test_extreme_single(self):
    for i in range(len(classes)):
      with self.subTest(c=classes[i]):
        self.assertEqual([classes_values[i]], solution(classes[i], [0], [0]))

  def test_extreme_double(self):
    last_class_index = len(classes) - 1

    for i in range(last_class_index):
      with self.subTest(c=classes[i]):
        self.assertEqual([classes_values[i], classes_values[i], classes_values[i + 1]],
                         solution(classes[i] + classes[i + 1], [0, 0, 1], [0, 1, 1]))

    with self.subTest(c=classes[last_class_index]):
      self.assertEqual([classes_values[last_class_index]] * 3,
                       solution(classes[last_class_index] * 2, [0, 0, 1], [0, 1, 1]))

  def test_simple(self):
    self.assertEqual([], solution('', [], []))
    self.assertEqual([], solution(classes[0], [], []))
    self.assertEqual([], solution(classes[0] + classes[1], [], []))

  def test_small_length_string(self):
    self.__test_random(10)

  def test_small_random(self):
    self.__test_random(300)

  # Performance

  def test_almost_all_same_letters(self):
    # GGGGGG..??..GGGGGG..??..GGGGGG
    self.__test_random_for('GGGGGGAC')
    self.__test_random_for('TAGGGGGGCT')
    self.__test_random_for('CAGGGGGG')

  def test_large_random(self):
    self.__test_random(MAX_N)

  def test_extreme_large(self):
    self.__test_random(MAX_N, MAX_M)

  # Utils

  @staticmethod
  def __brute_solution(s, start_pos, end_pos):
    s2 = [classes_map[c] for c in s]

    return [min(s2[start_pos[i]: end_pos[i] + 1]) for i in range(len(start_pos))]

  @staticmethod
  def __get_random_string(n=10):
    return ''.join(np.random.choice(classes, n))

  @staticmethod
  def __get_random_input_for(s, m=-1):
    n = len(s)

    if m < 0:
      # The max number of distinct valid tuples is not n^2 because end_pos < start_pos
      m = min(random.randint(1, sum_first_n_natural_numbers(n)), MAX_M)

    start_pos = np.random.random_integers(0, n - 1, m)
    end_pos = [random.randint(i, n - 1) for i in start_pos]
    return s, start_pos, end_pos

  def __get_random_input(self, n=10, m=-1):
    return self.__get_random_input_for(self.__get_random_string(n), m)

  def __test(self, test_input, **test_description):
    with self.subTest(**test_description):
      self.assertEqual(self.__brute_solution(*test_input), solution(*test_input))

  def __test_random(self, n=10, m=-1):
    random_input = self.__get_random_input(n, m)
    m = len(random_input[1])

    return self.__test(random_input, n=n, m=m)

  def __test_random_for(self, s, m=-1):
    random_input = self.__get_random_input_for(s, m)
    m = len(random_input[1])

    return self.__test(random_input, n=len(s), m=m)

if __name__ == '__main__':
  unittest.main()
