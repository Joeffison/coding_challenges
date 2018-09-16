#!/usr/bin/env python3

from math import sqrt
import fileinput
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange


def is_prime(n):
  if n == 2:
    return True
  elif n == 1 or n % 2 == 0:
    return False

  for i in range(3, int(sqrt(n)) + 2, 2):
    if n % i == 0:
      return False
  return True


def list_primes(start, end):
  if start < 3:
    start = 3
    yield 2
  elif start % 2 == 0:
    start += 1

  for i in range(start, end + 1, 2):
    if is_prime(i):
      yield i


if __name__ == '__main__':
  f_in = fileinput.input()

  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    m, n = map(int, f_in.readline().split())
    for prime in list_primes(m, n):
      print(prime)

    if i < n_test_cases - 1:
      print('')
