#!/usr/bin/env python3

import unittest

from challenges.filtered.demo.q001.degree_of_an_array_v001 import solution


class DegreeOfAnArrayTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual('2', solution([1, 2, 2, 3, 1]))


if __name__ == '__main__':
  unittest.main()
