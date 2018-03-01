#!/usr/bin/env python3

import random
import unittest

from tool_intro.codility.q001_v001 import *

MIN_RESULT = 1


def negative_list(end_value, ordered=False, start_value=-1):
  """
  Creates a lsit of negative values using the given range.

  :param end_value: Smallest value (inclusive)
  :param ordered: If false, array is shuffled
  :param start_value: Biggest value (inclusive). Default is -1.
  :return: List of negative values
  """
  response = list(range(start_value, end_value-1, -1))

  if not ordered:
    random.shuffle(response)
  return response


class CodilityTestCase(unittest.TestCase):

  def test_only_negatives(self):
    """
    Tests that lists (of length: |n| - 1)
    containing numbers between -1 and n
    return MIN_RESULT
    """
    for i in range(0, -10, -1):
      with self.subTest(i=i):
        self.assertEqual(solution(negative_list(i)), MIN_RESULT)


if __name__ == '__main__':
  unittest.main()
