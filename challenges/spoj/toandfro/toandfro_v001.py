#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()

  while True:
    n_columns = int(f_in.readline())
    if n_columns == 0:
      break

    encrypted = f_in.readline()[:-1]

    n = len(encrypted)
    # for i in range(n_columns):

    result = []
    k = 0

    for i in range(n // n_columns):
      if i % 2:
        if k:
          result.append(encrypted[k+n_columns-1:k-1:-1])
        else:
          result.append(encrypted[n_columns - 1::-1])
      else:
        result.append(encrypted[k:k + n_columns])
      k += n_columns

    solution = ""
    for i in range(n_columns):
      for j in range(n // n_columns):
        solution += result[j][i]
    print(solution)
