#!/usr/bin/env python3

import fileinput

operators = '+', '-', '*', '/', '^'


if __name__ == '__main__':
  f_in = fileinput.input()
  n_test_cases = int(f_in.readline())

  for i in range(n_test_cases):
    expression = (f_in.readline())[:-1]
    result = ''
    stack = []

    for c in expression:
      if c in operators or c == '(':
        stack.append(c)
      elif c == ')':
        while True:
          top = stack.pop()
          if top == '(':
            break
          else:
            result += top
      else:
        result += c
    print(result)
