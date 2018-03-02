#!/usr/bin/env python3

import unittest

from challenges.codility.lessons.q001_v001 import *


def to_bin(n):
  s = str(bin(n))[2:]
  if len(s) % 8:
    s = (8 - (len(s) % 8))*'0' + s
  return s


class CodilityTestCase(unittest.TestCase):

  def test_description_examples(self):
    # 00001001
    self.assertEqual(solution(9), 2)

    # 0000001000010001
    self.assertEqual(solution(529), 4)

    # 00010100
    self.assertEqual(solution(20), 1)

    # 00001111
    self.assertEqual(solution(15), 0)

    # 0000010000010001
    self.assertEqual(solution(1041), 5)

  def test_example1(self):
    # 0000010000010001
    self.assertEqual(solution(1041), 5)

  def test_example2(self):
    # 00001111
    self.assertEqual(solution(15), 0)

  def test_extremes(self):
    # 00000001
    self.assertEqual(solution(1), 0)

    # 00000101
    self.assertEqual(solution(5), 1)

    # 01111111111111111111111111111111 = 2 ** 31 - 1
    self.assertEqual(solution(2147483647), 0)

  def test_trailing_zeroes(self):
    # 00000110
    self.assertEqual(solution(6), 0)

    # 0000000101001000
    self.assertEqual(solution(328), 2)

  def test_power_of_2(self):
    # 00000101
    self.assertEqual(solution(5), 1)

    # 00010000
    self.assertEqual(solution(16), 0)

    # 00000100
    self.assertEqual(solution(1024), 0)

  def test_simple1(self):
    # 00001001
    self.assertEqual(solution(9), 2)

    # 00001011
    self.assertEqual(solution(11), 1)

  def test_simple2(self):
    # 00010011
    self.assertEqual(solution(19), 2)

    # 00101010
    self.assertEqual(solution(42), 1)

  def test_simple3(self):
    # 0000010010001010
    self.assertEqual(solution(1162), 3)

    # 00000101
    self.assertEqual(solution(5), 1)

  def test_medium1(self):
    # 1100101000000000
    self.assertEqual(solution(51712), 2)

    # 00010100
    self.assertEqual(solution(20), 1)

  def test_medium2(self):
    # 000010001001001011100100
    self.assertEqual(solution(561892), 3)

    # 00001001
    self.assertEqual(solution(9), 2)

  def test_medium3(self):
    # 000000010000010000000001
    self.assertEqual(solution(66561), 9)

  def test_large1(self):
    # 011000000000000000000001
    self.assertEqual(solution(6291457), 20)

  def test_large2(self):
    # 00000100011101101110100011100001
    self.assertEqual(solution(74901729), 4)

  def test_large3(self):
    # 00110000000000000000000000000001
    self.assertEqual(solution(805306369), 27)

  def test_large4(self):
    # 01010010000100000100000100010010
    self.assertEqual(solution(1376796946), 5)

  def test_large5(self):
    # 01000000000000000000000000000001
    self.assertEqual(solution(1073741825), 29)

  def test_large6(self):
    # 01100000000000000000000000000001
    self.assertEqual(solution(1610612737), 28)

  def test_input_0(self):
    # 00000000
    self.assertEqual(solution(0), 0)

if __name__ == '__main__':
  unittest.main()
