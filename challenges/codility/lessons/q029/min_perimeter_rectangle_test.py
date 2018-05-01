#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q029.min_perimeter_rectangle_v001 import *

MAX_N = 1000000000


class MinPerimeterRectangleTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.__sub_test(22, 30)

  # Correctness

  def test_extreme_min(self):
    self.__sub_test(4, 1)

  def test_simple1(self):
    self.__sub_test(24, 36)

  def test_simple2(self):
    self.__sub_test(28, 48)

  def test_simple3(self):
    self.__sub_test(204, 101)

  def test_small(self):
    self.__sub_test(1238, 1234)

  # Performance

  @timeout_decorator.timeout(0.150)
  def test_medium1(self):
    self.__sub_test(8552, 4564320)

  @timeout_decorator.timeout(0.150)
  def test_prime1(self):
    self.__sub_test(30972904, 15486451)

  @timeout_decorator.timeout(0.150)
  def test_square(self):
    self.__sub_test(40000, 100000000)

  @timeout_decorator.timeout(0.150)
  def test_prime2(self):
    self.__sub_test(1964903308, 982451653)

  @timeout_decorator.timeout(0.150)
  def test_extreme_max(self):
    self.__sub_test(126500, MAX_N)

  # Util

  def __sub_test(self, expected, n, **kwargs):
    if not kwargs:
      kwargs = {'result': expected, 'n':n}

    with self.subTest(**kwargs):
      self.assertEqual(expected, solution(n))


if __name__ == '__main__':
  unittest.main()
