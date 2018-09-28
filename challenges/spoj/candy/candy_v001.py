#!/usr/bin/env python3

import fileinput

if __name__ == '__main__':
  f_in = fileinput.input()
  while True:
    n = int(f_in.readline())
    if n < 0:
      break
    elif n == 0:
      print(-1)
    else:
      packets = []
      for i in range(n):
        packets.append(float(f_in.readline()))
      packets_avg = sum(packets)/len(packets)
      if int(packets_avg) < packets_avg:
        print(-1)
      else:
        print(int(sum([packets_avg - packet for packet in filter(lambda x: x <= packets_avg, packets)])))
