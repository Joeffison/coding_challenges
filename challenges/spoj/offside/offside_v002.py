#!/usr/bin/env python2

import fileinput

MAX_N = 10000


def read_integers_from_input():
  f_in = fileinput.input()
  for line in f_in:
    for number in line.split(' '):
      yield int(number)


if __name__ == '__main__':
  int_input = read_integers_from_input()

  while 1:
    n_attack = next(int_input)
    n_defense = next(int_input)

    if n_attack == 0 and n_defense == 0:
      break

    min_attack = min_defense = min_defense2 = (MAX_N + 1)
    for _ in range(n_attack):
      distance = next(int_input)
      if min_attack > distance:
        min_attack = distance

    for _ in range(n_defense):
      distance = next(int_input)
      if min_defense > distance:
        min_defense2 = min_defense
        min_defense = distance
      elif min_defense2 > distance:
        min_defense2 = distance

    print('Y' if min_attack < min_defense2 else 'N')
