def replace_negative(l, default_value=0):
  n_replaced = 0

  for i in range(len(l)):
    if l[i] < 0:
      l[i] = default_value
      n_replaced = n_replaced + 1

  return n_replaced


def solution(A):
  length = len(A)

  if replace_negative(A) is length:
    return 1

  for value in A:
    if (value is not 0) and (abs(value) - 1 < length) and (A[abs(value)-1] >= 0):
      A[abs(value) - 1] = -A[abs(value) - 1] if A[abs(value) - 1] is not 0 else -1

  for i in range(length):
    if A[i] >= 0:
      return i + 1

  return length + 1
