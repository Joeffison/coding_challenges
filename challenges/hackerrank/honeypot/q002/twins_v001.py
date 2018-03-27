#!/usr/bin/env python3


def __twins(a, b):
  even_a = a[::2]
  odd_a = a[1::2]
  even_a = sorted(even_a)
  odd_a = sorted(odd_a)

  even_b = b[::2]
  odd_b = b[1::2]
  even_b = sorted(even_b)
  odd_b = sorted(odd_b)
  return 'Yes' if (even_a == even_b) and (odd_a == odd_b) else 'No'


def twins(a, b):
  return [__twins(a[i], b[i]) for i in range(len(a))]


"""
#!/bin/python3

import sys
import os

# Complete the function below.

def twins(a, b):


if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a_cnt = 0
    a_cnt = int(input())
    a_i = 0
    a = []
    while a_i < a_cnt:
        try:
            a_item = str(input())
        except:
            a_item = None
        a.append(a_item)
        a_i += 1


    b_cnt = 0
    b_cnt = int(input())
    b_i = 0
    b = []
    while b_i < b_cnt:
        try:
            b_item = str(input())
        except:
            b_item = None
        b.append(b_item)
        b_i += 1


    res = twins(a, b);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )


    f.close()
"""
