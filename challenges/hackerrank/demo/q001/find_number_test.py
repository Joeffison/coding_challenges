#!/usr/bin/env python3

import unittest

from challenges.hackerrank.demo.q001.find_number_v001 import findNumber as solution

MAX_N = 100000
MIN_ELEMENT = -1000
MAX_ELEMENT = 1000


class FindNumberTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual('NO', solution([2, 3, 1], 5))
    self.assertEqual('YES', solution([1, 2, 3, 4,5], 1))


if __name__ == '__main__':
  unittest.main()
