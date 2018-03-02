#!/usr/binMAX_VALUEenv python3

import unittest

from tool_intro.codility.lessons.q005_v001 import *

MAX_VALUE = 1000000000


def brute_solution(x, y, jump_size):
  return (y - x) // jump_size + (1 if (y - x) % jump_size else 0)


class Codility5TestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertEqual(solution(10, 85, 30), 3)

  def test_extreme_position(self):
    self.assertEqual(solution(85, 85, 1), 0)

  def test_small_extreme_jump(self):
    x, y, jump_size = 1, MAX_VALUE, MAX_VALUE - 1
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

  def test_many_jump1(self):
    x, y, jump_size = 1, MAX_VALUE, 2
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

  def test_many_jump2(self):
    x, y, jump_size = 1, MAX_VALUE, 99
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

  def test_many_jump3(self):
    x, y, jump_size = 1, MAX_VALUE, 1283
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

  def test_big_extreme_jump(self):
    x, y, jump_size = 1, MAX_VALUE, 1
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

  def test_small_jumps(self):
    x, y, jump_size = 1, MAX_VALUE, 13
    self.assertEqual(solution(x, y, jump_size), brute_solution(x, y, jump_size))

if __name__ == '__main__':
  unittest.main()
