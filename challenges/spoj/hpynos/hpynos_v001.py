#!/usr/bin/env python3

import fileinput


def break_number(n):
  result = 0

  while n:
    current_digit = n % 10
    result += current_digit * current_digit
    n //= 10

  return result


def is_happy(n):
  steps = 0
  intermediate = []
  current = n

  while True:
    if current in intermediate:
      return -1
    elif current == 1:
      return steps

    intermediate.append(current)
    current = break_number(current)
    steps += 1


if __name__ == '__main__':
  print(is_happy(int(fileinput.input().readline())))
