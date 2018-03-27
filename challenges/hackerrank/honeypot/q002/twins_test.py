#!/usr/bin/env python3

import unittest

from challenges.hackerrank.honeypot.q002.twins_v001 import twins as solution

MAX_N = 100000
MIN_ELEMENT = -1000
MAX_ELEMENT = 1000


class TwinsTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(['Yes', 'No', 'No'], solution(['cdab', 'dcba', 'abcd'], ['abcd', 'abcd', 'abcdcd']))
    self.assertEqual(['Yes', 'Yes'], solution(['abbc', 'abbdd'], ['abbc', 'ddbba']))
    self.assertEqual(['No'], solution(['av'], ['ab']))


if __name__ == '__main__':
  unittest.main()
