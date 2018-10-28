#!/usr/bin/env python3

import fileinput


def read_integers_from_input():
  for line in fileinput.input():
    line = line.strip()

    if line:
      for number in line.split(' '):
        yield int(number)


if __name__ == '__main__':
  int_input = read_integers_from_input()
  n_test_cases = next(int_input)
  sum_result = 0

  for i in range(1, n_test_cases + 1):
    n_stamps, n_friends = next(int_input), next(int_input)
    friends = []

    j, sum_result = 0, 0
    if n_stamps == 0 or n_friends == 0:
      # discard input
      while n_friends:
        n_friends -= 1
        next(int_input)
    else:
      for j in range(n_friends):
        friends.append(next(int_input))

      # as the stamp counts are ordered in descending order,
      # j will be the minimum number of friends from whom Lucy can borrow stamps
      friends.sort(reverse=True)
      for j in range(1, n_friends + 1):
        sum_result += friends[j - 1]
        if sum_result >= n_stamps:
          break

    if sum_result < n_stamps:
      print("Scenario #%d:\nimpossible\n" % i)
    else:
      print("Scenario #%d:\n%d\n" % (i, j))
