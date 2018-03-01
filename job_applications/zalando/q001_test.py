#!/usr/bin/env python3

import unittest

from job_applications.zalando.q001_v002 import *


class ZalandoQ001TestCase(unittest.TestCase):

  def test_input1(self):
    self.assertEqual(solution(1, 1, 2, 3), 5)

  def test_input2(self):
    self.assertEqual(solution(2, 4, 2, 4), 8)


if __name__ == '__main__':
  unittest.main()
