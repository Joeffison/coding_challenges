def solution(A):
  i = 1
  s = []
  for value in A:
    s.append(value)
    if value == i:
      while True:
        value = value + 1
        if value not in s:
          break
      i = value
  return i
