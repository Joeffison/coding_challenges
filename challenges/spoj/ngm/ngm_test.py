#!/usr/bin/env python3

import unittest

from challenges.spoj.ngm.ngm_v001 import solution


class AGameWithNumbersTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(solution(14), "1\n4")

  def test_simple(self):
    for i in range(1, 10):
      self.assertEqual(solution(i * 10), "2")
      self.assertEqual(solution(i * 10 + i), "1\n" + str(i))
      self.assertEqual(solution(i), "1\n" + str(i))


if __name__ == '__main__':
  unittest.main()
