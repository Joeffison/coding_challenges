#!/usr/bin/env python3

import unittest

from job_applications.zalando.q002.q002_v001 import *


class ZalandoQ002TestCase(unittest.TestCase):

  def test_empty_input(self):
    self.assertEqual(solution(''), 0)

  def test_input1(self):
    self.assertEqual(solution('(())'), 2)

  def test_input2(self):
    self.assertEqual(solution('(())))('), 4)

  def test_input3(self):
    self.assertEqual(solution('))'), 2)

  def test_input4(self):
    self.assertEqual(solution('(('), 0)


if __name__ == '__main__':
  unittest.main()
