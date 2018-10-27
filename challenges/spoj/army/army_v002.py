#!/usr/bin/env python2

import fileinput


def read_integers_from_input():
  for line in fileinput.input():
    if line.strip():
      for number in line.split(' '):
        yield int(number)


if __name__ == '__main__':
  ARMY_1 = 'Godzilla'
  ARMY_2 = 'MechaGodzilla'
  NO_ANSWER = 'uncertain'

  int_input = read_integers_from_input()
  n_test_cases = next(int_input)

  for i in xrange(n_test_cases):
    n_army_1, n_army_2 = next(int_input), next(int_input)

    if n_army_1 == 0:
      if n_army_2 == 0:
        print(NO_ANSWER)
      else:
        print(ARMY_2)

        # discard input
        while n_army_2:
          n_army_2 -= 1
          next(int_input)
    elif n_army_2 == 0:
      print(ARMY_1)

      # discard input
      while n_army_1:
        n_army_1 -= 1
        next(int_input)
    else:
      # get strongest in army1
      strongest_army_1 = next(int_input)
      n_army_1 -= 1
      while n_army_1:
        n_army_1 -= 1
        temp = next(int_input)

        if temp > strongest_army_1:
          strongest_army_1 = temp

      # get strongest in army2
      strongest_army_2 = next(int_input)
      n_army_2 -= 1
      while n_army_2:
        n_army_2 -= 1
        temp = next(int_input)

        if temp > strongest_army_2:
          strongest_army_2 = temp

      if strongest_army_2 > strongest_army_1:
        print(ARMY_2)
      else:
        print(ARMY_1)
