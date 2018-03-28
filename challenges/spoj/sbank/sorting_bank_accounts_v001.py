#!/usr/bin/env python3

# Hit compile and run to see a sample output.
# Read values from stdin, do NOT hard code input.

import fileinput
import sys
from collections import Counter


def solution(array):
  # Counts the element in the list
  counts = Counter(array)

  # Removes duplicates and sorts arry with TimSort (current python implmentation, which is slightly better than mergeSort)
  unique = list(set(array))
  unique.sort()

  # Prepares an array with the response, where response[i] is the ith ordered item followed by the number of times it is present in the original list
  response = [item.replace('\n', '') + ' ' + str(counts[item]) for item in unique]

  # The line below finally combines the response input in the format requested
  return '\n'.join(response) + '\n\n'

if __name__ == '__main__':
  n_tests = -1
  input_size = -1
  input_array = []
  i = 0
  last_computed = False

  # just realized I should have done this below with a simple for in range after reading first line, but as copy and paste are disabled, I won't fix it.
  for line in fileinput.input():
    if n_tests == -1:
      n_tests = line
    elif input_size == -1:
      input_size = int(line)
    elif i < input_size:
      i += 1
      input_array.append(line)
      last_computed = False
    else:
      sys.stdout.write(solution(input_array))
      last_computed = True
      i = 0
      input_size = -1
      input_array = []

  if not last_computed:
    sys.stdout.write(solution(input_array))
