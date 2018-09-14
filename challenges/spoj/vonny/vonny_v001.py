#!/usr/bin/env python2

import fileinput
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]

used_tiles = [[0] * 7 for i in range(7)]
visited_box_position = [[0] * 8 for i in range(7)]
box_of_tiles = []


def count_solutions(row=0, column=0):
  if column == 8:
    column = 0
    row += 1

  if row == 7:  # End of box reached
    return 1
  elif visited_box_position[row][column]:
    return count_solutions(row, column + 1)

  n_solutions = 0

  try:
    candidate = box_of_tiles[row][column], box_of_tiles[row][column + 1]
    if not visited_box_position[row][column + 1] and not used_tiles[candidate[0]][candidate[1]]:
      used_tiles[candidate[0]][candidate[1]] = 1
      used_tiles[candidate[1]][candidate[0]] = 1

      visited_box_position[row][column] = 1
      visited_box_position[row][column + 1] = 1

      # print row, column, candidate
      n_solutions += count_solutions(row, column + 2)

      visited_box_position[row][column] = 0
      visited_box_position[row][column + 1] = 0

      used_tiles[candidate[0]][candidate[1]] = 0
      used_tiles[candidate[1]][candidate[0]] = 0
  except:
    pass

  try:
    candidate = box_of_tiles[row][column], box_of_tiles[row + 1][column]
    if not visited_box_position[row + 1][column] and not used_tiles[candidate[0]][candidate[1]]:
      used_tiles[candidate[0]][candidate[1]] = 1
      used_tiles[candidate[1]][candidate[0]] = 1

      visited_box_position[row][column] = 1
      visited_box_position[row + 1][column] = 1

      # print row, column, candidate

      n_solutions += count_solutions(row, column + 1)

      visited_box_position[row][column] = 0
      visited_box_position[row + 1][column] = 0

      used_tiles[candidate[0]][candidate[1]] = 0
      used_tiles[candidate[1]][candidate[0]] = 0
  except:
    pass

  return n_solutions


if __name__ == '__main__':
  f_in = fileinput.input()

  n_test_cases = int(f_in.readline())

  for test_case in range(n_test_cases):
    box_of_tiles = []
    for line in range(7):
      box_of_tiles.append(map(int, f_in.readline().split()))

    print(count_solutions())

    f_in.readline()
