#!/usr/bin/env python3

import unittest

from challenges.hackerrank.demo.q002.odd_numbers_v001 import oddNumbers as solution

MAX_N = 100000
MIN_ELEMENT = -1000
MAX_ELEMENT = 1000


class OddNumbersTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual([3, 5], solution(2, 5))
    self.assertEqual([3, 5, 7, 9], solution(3, 9))


if __name__ == '__main__':
  unittest.main()
