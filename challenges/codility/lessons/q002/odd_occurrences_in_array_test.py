#!/usr/bin/env python3

import unittest

from challenges.codility.lessons.q002.odd_occurrences_in_array_v001 import *


def get_random_odd_list(n):
  """
    Creates a random list with only one element that occurs an odd number of times

  :param n: Size of the resulting list
  :return:
    N-sized random list with only one element occurring an odd number of times
    and the odd occurring element
  """

  import numpy as np
  import random

  # Creates a list with n/2 + 1 elements
  array = (np.random.random_integers(1, 1000000000, (1, n//2 + 1))[0]).tolist()

  # Picks one of the elements to be the odd occurring element
  odd = random.choice(array)

  # Duplicates only the other elements
  array.remove(odd)
  array = array + [odd] + array

  # Shuffles the resulting list
  random.shuffle(array)

  return odd, array


class OddOccurrencesInArrayTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

  def test_example1(self):
    self.assertEqual(solution([9, 3, 9, 3, 9, 7, 9]), 7)

  def test_simple1(self):
    expected_element, list = get_random_odd_list(5)
    self.assertEqual(solution(list), expected_element)

  def test_simple2(self):
    expected_element, list = get_random_odd_list(11)
    self.assertEqual(solution(list), expected_element)

  def test_extreme_single_item(self):
    self.assertEqual(solution([42]), 42)

  def test_small1(self):
    expected_element, list = get_random_odd_list(201)
    self.assertEqual(solution(list), expected_element)

  def test_small2(self):
    expected_element, list = get_random_odd_list(601)
    self.assertEqual(solution(list), expected_element)

  def test_medium1(self):
    expected_element, list = get_random_odd_list(2001)
    self.assertEqual(solution(list), expected_element)

  def test_medium2(self):
    expected_element, list = get_random_odd_list(100003)
    self.assertEqual(solution(list), expected_element)

  def test_big1(self):
    expected_element, list = get_random_odd_list(999999)
    self.assertEqual(solution(list), expected_element)

  def test_big2(self):
    expected_element, list = get_random_odd_list(999999)
    self.assertEqual(solution(list), expected_element)

if __name__ == '__main__':
  unittest.main()
