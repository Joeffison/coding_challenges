#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q019.stone_wall_v001 import *

MAX_N = 100000
MIN_ELEMENT = 1
MAX_ELEMENT = 1000000000


class StoneWallTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(7, solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))

  # Correctness

  def test_simple_1(self):
    self.assertEqual(1, solution([888]))

  def test_simple_2(self):
    self.assertEqual(1, solution([888, 888]))

  def test_simple_3(self):
    self.assertEqual(3, solution([888, 1, 888]))

  def test_simple_4(self):
    self.assertEqual(3, solution([5, 5, 4, 5]))
    self.assertEqual(3, solution([5, 5, 4, 4, 5]))

  def test_boundary_cases(self):
    n = 1000
    self.assertEqual(n - MIN_ELEMENT + 1, solution((range(MIN_ELEMENT, n + 1))))

  # Performance

  @timeout_decorator.timeout(0.015)
  def test_medium1(self):
    self.assertEqual(8, solution([4, 5, 6, 7, 7, 7, 8, 1, 3, 2]))

  @timeout_decorator.timeout(0.015)
  def test_medium2(self):
    self.assertEqual(3, solution([1, 2, 2, 1, 1, 1, 1, 1, 1, 2]))

  @timeout_decorator.timeout(0.015)
  def test_medium3(self):
    self.assertEqual(6, solution([17, 1, 17, 2, 2, 5, 5, 2, 5, 5]))

  @timeout_decorator.timeout(0.015)
  def test_medium4(self):
    self.assertEqual(15, solution([17, 5, 19, 69, 5, 10, 19, 92, 24, 11, 19, 95, 16, 8, 19, 68]))

  @timeout_decorator.timeout(0.350)
  def test_large_pyramid(self):
    start = 1
    end = 17000
    array = list(range(start, end + 1)) + list(range(end, start - 1, -1))
    self.assertEqual(end - start + 1, solution(array))

  @timeout_decorator.timeout(0.650)
  def test_large_increasing_decreasing(self):
    start = 2
    end = 20000
    array = list(range(start, end + 1, 2)) + list(range(end, start - 1, -2))
    self.assertEqual((end - start) // 2 + 1, solution(array))

    start = 3
    end = 21000
    array = list(range(start, end + 1, 3)) + list(range(end, start - 1, -3))
    self.assertEqual((end - start) // 3 + 1, solution(array))

  @timeout_decorator.timeout(0.350)
  def test_large_up_to_20(self):
    self.__test_sequence(200)

  @timeout_decorator.timeout(0.350)
  def test_large_up_to_100(self):
    self.__test_sequence(1000)

  @timeout_decorator.timeout(0.350)
  def test_large_max(self):
    self.__test_sequence(10000)

  def __test_sequence(self, n, start=MIN_ELEMENT):
    self.assertEqual(n, solution(range(start, start + n)))


if __name__ == '__main__':
  unittest.main()
