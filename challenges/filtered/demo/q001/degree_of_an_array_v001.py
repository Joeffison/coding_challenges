#!/usr/bin/env python3

#Hit compile and run to see a sample output.
#Read values from stdin, do NOT hard code input.

"""
import fileinput
import sys
"""


def solution(array):
  # maps the number of occurrence of each element and the first and last index it occurs
  count_map = {}

  # current max number of occurrences of a value
  max_count = 0

  # length of current shortest list with an element with number repetitions equal to max_count
  min_sub_array = 0

  for i in range(len(array)):
    item = array[i]

    # the code below initializes a key on our dict, in case we didn't see this item before
    if item not in count_map:
      count_map[item] = {
        'count': 0,
        'first_seen': i,
        'last_seen': i
      }

    # updates the values in our dict accordingly
    current = count_map[item]
    current['count'] += 1
    current['last_seen'] = i

    # in case this item occurs more than *max_count* times, we update our current answer
    if current['count'] > max_count:
      max_count = current['count']
      min_sub_array = current['last_seen'] - current['first_seen'] + 1

    # we've got to check when an item occurs *max_count* times as well,
    # because the interval between its first and last index might be smaller than what we have seen
    elif current['count'] == max_count and (current['last_seen'] - current['first_seen'] + 1) < min_sub_array:
      min_sub_array = current['last_seen'] - current['first_seen'] + 1

  return str(min_sub_array)

"""
i = 0
for line in fileinput.input():
    if i % 2 == 1:
        sys.stdout.write(solution(line.split(' ')))
    i += 1
"""
