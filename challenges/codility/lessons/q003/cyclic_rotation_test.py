#!/usr/bin/env python3

import unittest

from challenges.codility.lessons.q003.cyclic_rotation_v001 import *


class CyclicRotationTestCase(unittest.TestCase):

  def test_description_examples(self):
    original_list = [3, 8, 9, 7, 6]
    for i in range(0, len(original_list) * 4, len(original_list)):
      n_rotations = 0
      with self.subTest(original_list=original_list, n_rotations=i + n_rotations):
        self.assertEqual(solution(original_list, i + n_rotations), original_list)

      n_rotations += 1
      with self.subTest(original_list=original_list, n_rotations=i + n_rotations):
        self.assertEqual(solution(original_list, i + n_rotations), [6, 3, 8, 9, 7])

      n_rotations += 1
      with self.subTest(original_list=original_list, n_rotations=i + n_rotations):
        self.assertEqual(solution(original_list, i + n_rotations), [7, 6, 3, 8, 9])

      n_rotations += 1
      with self.subTest(original_list=original_list, n_rotations=i + n_rotations):
        self.assertEqual(solution(original_list, i + n_rotations), [9, 7, 6, 3, 8])

    original_list = [0, 0, 0]
    n_rotations = 1
    with self.subTest(original_list=original_list, n_rotations=n_rotations):
      self.assertEqual(solution(original_list, n_rotations), original_list)

    original_list = [1, 2, 3, 4]
    n_rotations = len(original_list)
    with self.subTest(original_list=original_list, n_rotations=n_rotations):
      self.assertEqual(solution(original_list, n_rotations), original_list)

  def test_extreme_empty(self):
    self.assertEqual(solution([], 0), [])
    self.assertEqual(solution([], 1), [])
    self.assertEqual(solution([], 9), [])

  def test_single(self):
    original_list = [8]
    for i in range(6):
      with self.subTest(original_list=original_list, n_rotations=i):
        self.assertEqual(solution(original_list, i), original_list)

  def test_double(self):
    original_list = [89, 3]
    with self.subTest(original_list=original_list, n_rotations=0):
      self.assertEqual(solution(original_list, 0), original_list)

    with self.subTest(original_list=original_list, n_rotations=1):
      self.assertEqual(solution(original_list, 1), [3, 89])

    with self.subTest(original_list=original_list, n_rotations=2):
      self.assertEqual(solution(original_list, 2), original_list)

  def test_small2(self):
    self.assertEqual(solution([1, 1, 2, 3, 5], 42), [3, 5, 1, 1, 2])

  def test_maximal(self):
    import numpy as np

    MAX_N = 100
    MAX_K = 100
    MIN_ELEMENT = -1000
    MAX_ELEMENT = 1000

    max_list = list(np.random.random_integers(MIN_ELEMENT, MAX_ELEMENT, (1, MAX_N)))
    self.assertEqual(solution(max_list, MAX_K), max_list)

if __name__ == '__main__':
  unittest.main()
