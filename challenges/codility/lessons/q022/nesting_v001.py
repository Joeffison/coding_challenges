#!/usr/bin/env python3
from util.challenges.string_challenges import check_matching_brackets


def solution(s):
  """
  Check if a string has properly matching brackets

  :param s: String to verify if it is well-formed
  :return: 1 if the brackets are properly matching, 0 otherwise
  """

  return check_matching_brackets(s, opening="(", closing=")")
