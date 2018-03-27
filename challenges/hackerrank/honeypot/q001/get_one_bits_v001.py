#!/usr/bin/env python3


def getOneBits(n):
  bit_mask = 0x100000000000000000000000000000
  saw_first_one = False
  result = []
  index = 1

  while bit_mask > 0:
    if saw_first_one:
      index += 1

    if n & bit_mask:
      saw_first_one = True
      result.append(index)

    # we now use a left shift to move the bit 1 one position to the left
    bit_mask >>= 1
  return [len(result)] + result

"""
#!/bin/python3

import sys
import os

# Complete the function below.

def getOneBits(n):


if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    res = getOneBits(n);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()
"""
