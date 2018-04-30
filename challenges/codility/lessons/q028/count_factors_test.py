#!/usr/bin/env python3

import unittest
from math import factorial, pow

import timeout_decorator

from challenges.codility.lessons.q028.count_factors_v001 import *

MAX_N = 2147483647


class CountFactorsTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.__sub_test(8, factorial(4))

  # Correctness

  def test_squares(self):
    self.__sub_test(5, 16)
    self.__sub_test(9, 36)

  def test_tiny(self):
    self.__sub_test(1, 1)
    self.__sub_test(2, 2)
    self.__sub_test(2, 3)
    self.__sub_test(3, 4)
    self.__sub_test(2, 5)
    self.__sub_test(4, 6)
    self.__sub_test(2, 7)
    self.__sub_test(4, 8)
    self.__sub_test(3, 9)
    self.__sub_test(4, 10)

  def test_simple1(self):
    self.__sub_test(2, 41)
    self.__sub_test(8, 42)

  def test_simple2(self):
    self.__sub_test(4, 69)
    self.__sub_test(7, 64)
    self.__sub_test(16, factorial(5))

  def test_simple3(self):
    self.__sub_test(30, factorial(6))
    self.__sub_test(4, 1111)

  def test_simple4(self):
    self.__sub_test(60, factorial(7))
    self.__sub_test(8, 12345)

  def test_simple5(self):
    self.__sub_test(4, 34879)
    self.__sub_test(96, factorial(8))

  def test_extreme_one(self):
    self.__sub_test(1, 1)

  # Performance

  @timeout_decorator.timeout(0.150)
  def test_medium1(self):
    self.__sub_test(160, factorial(9))
    self.__sub_test(16, 1948102)

  @timeout_decorator.timeout(0.150)
  def test_medium2(self):
    self.__sub_test(270, factorial(10))
    self.__sub_test(12, 5621892)
    self.__sub_test(45, 4999696)

  @timeout_decorator.timeout(0.150)
  def test_big1(self):
    self.__sub_test(4, 27043111)
    self.__sub_test(540, factorial(11))
    self.__sub_test(135, 39992976)

  @timeout_decorator.timeout(0.150)
  def test_big2(self):
    self.__sub_test(96, 97093212)
    self.__sub_test(29, pow(2, 28))

  @timeout_decorator.timeout(0.150)
  def test_big3(self):
    self.__sub_test(792, factorial(12))
    self.__sub_test(2, 780291637)
    self.__sub_test(15, 449991369)

  @timeout_decorator.timeout(0.150)
  def test_extreme_maxint(self):
    self.__sub_test(100, 1000000000)
    self.__sub_test(2, MAX_N)
    self.__sub_test(135, 2147395600)

  # Util

  def __sub_test(self, expected, n, **kwargs):
    if not kwargs:
      kwargs = {'result': expected, 'n':n}

    with self.subTest(**kwargs):
      self.assertEqual(expected, solution(n))


if __name__ == '__main__':
  unittest.main()
