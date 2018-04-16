#!/usr/bin/env python3

import unittest

import timeout_decorator

from challenges.codility.lessons.q020.brackets_v001 import *

MAX_N = 200000


class NestingTestCase(unittest.TestCase):

  def test_description_examples(self):
    self.assertTrue(solution("(()(())())"))
    self.assertFalse(solution("())"))

  # Correctness

  def test_negative_match(self):
    # invalid structure, but the number of parentheses matches
    self.assertFalse(solution(")("))
    self.assertFalse(solution(")()("))

  def test_empty(self):
    self.assertTrue(solution(""))

  def test_simple_grouped(self):
    # simple grouped positive and negative test, length=22
    self.assertTrue(solution("()()()()()()()()()()()"))
    self.assertTrue(solution("((((((((((()))))))))))"))
    self.assertFalse(solution("()()()()()()()()()())("))
    self.assertTrue(solution("(((((((((()))())))))))"))
    self.assertTrue(solution("(((())))(((())))((()))"))

  # Performance

  @timeout_decorator.timeout(1.084)
  def test_large1(self):
    # simple large positive test, 100K ('s followed by 100K )'s + )(
    n = MAX_N
    self.assertTrue(solution(n//2 * "(" + n//2 * ")"))
    self.assertFalse(solution(n//2 * "(" + n//2 * ")" + ")("))
    self.assertTrue(solution(n//2 * "(" + n//2 * ")" + "()"))

  @timeout_decorator.timeout(0.350)
  def test_large2(self):
    # simple large negative test, 10K+1 ('s followed by 10K )'s + )( + ()
    n = 20000
    self.assertTrue(solution((n//2 + 1) * "(" + n//2 * ")" + ")(())"))
    self.assertFalse(solution((n//2 + 1) * "(" + n//2 * ")" + ")(()"))
    self.assertTrue(solution((n//2 + 1) * "(" + n//2 * ")" + ")(())(())"))

  @timeout_decorator.timeout(0.450)
  def test_large_full_ternary_tree(self):
    # tree of the form T=(TTT) and depth 11, length=177K+
    self.assertTrue(solution(self.__tree(11, "((((((((((((((()))))))))))))))", 3)))

  @timeout_decorator.timeout(0.550)
  def test_multiple_full_binary_trees(self):
    # sequence of full trees of the form T=(TT), depths (1..10..1), with/without some brackets at the end, length=49K+
    self.assertTrue(solution(self.__tree(10, "(((((((((((())))))))))))")))
    self.assertFalse(solution(self.__tree(10, "(((((((((((())))))))))))") + ")"))
    self.assertTrue(solution(self.__tree(10, "(((((((((((())))))))))))") + "(())"))
    self.assertTrue(solution(self.__tree(10, "(((((((((((())))))))))))") + "((()))"))
    self.assertFalse(solution(self.__tree(10, "(((((((((((())))))))))))") + "())"))

  @timeout_decorator.timeout(1.350)
  def test_broad_tree_with_deep_paths(self):
    # string of the form (TTT...T) of 300 T's, each T being '(((...)))' nested 200-fold, length=120K+
    t = 200*"(((" + 200*")))"
    self.assertTrue(solution(t*300))
    self.assertTrue(solution(t*301))

  def __tree(self, depth, node="()", n=2):
    if depth < 0:
      return ""
    return node + self.__tree(depth - 1, node)*n


if __name__ == '__main__':
  unittest.main()
