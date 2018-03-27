#!/usr/bin/env python3

import unittest

from challenges.hackerrank.honeypot.q001.get_one_bits_v001 import getOneBits as solution

MAX_VALUE = 1000000000


class GetOneBitsTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual([3, 1, 3, 8], solution(161))
    self.assertEqual([3, 1, 4, 6], solution(37))

  def test_extreme(self):
    self.assertEqual([13, 1, 2, 3, 5, 6, 7, 10, 11, 13, 15, 16, 19, 21],
                     solution(MAX_VALUE))

if __name__ == '__main__':
  unittest.main()
