#!/usr/bin/env python3

import random
import unittest

from challenges.codility.lessons.q007.permutation_check_v001 import *

MIN_ELEMENT = 1
MAX_ELEMENT = 1000000000


class PermutationCheckTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(1, solution([4, 1, 3, 2]))
    self.assertEqual(0, solution([4, 1, 3]))

  def test_example1(self):
    self.assertEqual(1, solution([4, 1, 3, 2]))

  def test_example2(self):
    self.assertEqual(0, solution([4, 1, 3]))

  # Correctness

  def test_extreme_min_max(self):
    self.assertEqual(1, solution([MIN_ELEMENT]))
    self.assertEqual(0, solution([100]))

  def test_single(self):
    array = [1]
    with self.subTest():
      self.assertEqual(1, solution(array))

    array = [2]
    with self.subTest():
      self.assertEqual(0, solution(array))

  def test_double(self):
    array = [2, 1]
    with self.subTest():
      self.assertEqual(1, solution(array))

    array = [1, 2]
    with self.subTest():
      self.assertEqual(1, solution(array))

    array = [1, 3]
    with self.subTest():
      self.assertEqual(0, solution(array))

    array = [3, 1]
    with self.subTest():
      self.assertEqual(0, solution(array))

  def test_anti_sum1(self):
    # total sum is correct, but it is not a permutation, N <= 10
    self.__test_anti_sum(10)

  def test_small_permutation(self):
    # permutation + one element occurs twice, N = ~100
    self.__test_permutation_plus_duplicated_values(100, 1)

  # Performance

  def test_medium_permutation(self):
    # permutation + few elements occur twice, N = ~10,000
    self.__test_permutation_plus_duplicated_values(10000, 3)

  def test_anti_sum2(self):
    # total sum is correct, but it is not a permutation, N = ~100,000
    self.__test_anti_sum(100000)

  def test_large_not_permutation(self):
    # permutation + one element occurs three times, N = ~100,000
    self.__test_permutation_plus_duplicated_values(100000, 3, single_duplicated=True)

  def test_large_range(self):
    # sequence 1, 2, ..., N, N = ~100,000
    n = 100000
    self.assertEqual(1, solution(list(range(1, n + 1))))

  def test_extreme_values(self):
    # all the same values, N = ~100,000
    n = 100000
    for i in range(3):
      duplicated = random.randint(MIN_ELEMENT, n)
      with self.subTest(n=n, duplicated=duplicated):
        self.assertEqual(0, solution([duplicated] * n))

  def test_various_permutations(self):
    # all sequences are permutations
    n = 100000
    for i in range(n - 4, n + 1):
      array = list(range(1, i))

      with self.subTest(n=i):
        self.assertEqual(1, solution(array))

  # Utils

  def __test_permutation_plus_duplicated_values(self, n, n_duplications=1, n_tests=2, single_duplicated=False):
    for i in range(n_tests):
      array = list(range(1, n + 1))
      duplicated = [random.choice(array)] * n_duplications if single_duplicated \
        else [random.choice(array) for i in range(n_duplications)]
      array += duplicated
      random.shuffle(array)

      with self.subTest(duplicated=duplicated):
        self.assertEqual(0, solution(array))

  def __test_anti_sum(self, n=10):
    # total sum is correct, but it is not a permutation.

    for i in range(n - 3, n + 1):
      array = list(range(1, n + 1))
      delta = random.randint(1, i)
      array[array.index(i)] = i - delta
      array[array.index(i-1)] = i + delta

      with self.subTest(i=i, delta=delta):
        self.assertEqual(0, solution(array))

if __name__ == '__main__':
  unittest.main()
