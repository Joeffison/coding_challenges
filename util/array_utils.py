#!/usr/bin/env python3
import random


def remove_random(array, all_occurrences=False):
  to_remove = array.pop(random.randint(1, len(array) - 1))

  if all_occurrences:
    while to_remove in array:
      array.remove(to_remove)

  return to_remove
