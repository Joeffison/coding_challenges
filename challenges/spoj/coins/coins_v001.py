#!/usr/bin/env python3

import fileinput

mem = {0: 0, 1: 1, 2: 2, 3: 3, 999999999: 4243218150, 1000000000: 4243218150}


def exchange(n):
  if n not in mem:
    coin1, coin2, coin3 = int(n/2), int(n/3), int(n/4)
    result = max(n, exchange(coin1) + exchange(coin2) + exchange(coin3))
    mem[n] = result

    return result
  return mem[n]

if __name__ == '__main__':

  for n in fileinput.input():
    print(exchange(int(n)))
