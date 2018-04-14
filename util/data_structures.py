class Stack():
  def __init__(self):
    self.array = []

  def push(self, item):
    self.array.append(item)

  def pop(self):
    return self.array.pop()

  def tail(self, n=1):
    return self.array[-n:]

  def length(self):
    return len(self.array)
