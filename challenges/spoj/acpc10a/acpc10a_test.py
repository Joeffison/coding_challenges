#!/usr/bin/env python3

import unittest

from challenges.spoj.acpc10a.acpc10a_v001 import solution


class WhatsNextTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(solution(4, 7, 10), "AP 13")
    self.assertEqual(solution(2, 6, 18), "GP 54")


if __name__ == '__main__':
  unittest.main()
