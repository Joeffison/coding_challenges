#!/usr/bin/env python3

import fileinput
import sys


def solution(n):
  # If a player faces a number n <= 9, they can play it to win
  # But if n is 10, there is no chance to win
  # and any number divisible per 10 will eventually lead to the same scenario (when both players are optimal)
  remainder = n % 10
  return "1\n" + str(remainder) if remainder != 0 else "2"


if __name__ == '__main__':
  f_in = fileinput.input()
  print(solution(int(f_in.readline())))
