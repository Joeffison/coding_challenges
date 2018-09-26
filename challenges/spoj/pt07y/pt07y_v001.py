#!/usr/bin/env python3

import fileinput
import sys

if sys.version_info[0] >= 3:
  map = lambda func, l: [func(i) for i in l]
else:
  range = xrange


class Tree:
  def __init__(self, n_vertices):
    self.adjacency = [[] for _ in range(n_vertices)]

  def add_edge(self, u, v):
    u -= 1
    v -= 1
    if v in self.adjacency[u]:
      raise Exception

    self.adjacency[u].append(v)
    self.adjacency[v].append(u)

  def is_tree(self):
    self.visited = [False for i in range(len(self.adjacency))]

    try:
      self.dfs(0)
      return all(self.visited)
    except:
      return False

  def dfs(self, u, previous=-1):
    if self.visited[u]:
      raise Exception

    self.visited[u] = True
    for vertex in self.adjacency[u]:
      if vertex != previous:
        self.dfs(vertex, u)


if __name__ == '__main__':
  f_in = fileinput.input()
  n_vertices, n_edges = map(int, f_in.readline().split())
  tree = Tree(n_vertices)

  try:
    for i in range(n_edges):
      tree.add_edge(*map(int, f_in.readline().split()))
    print('YES' if tree.is_tree() else 'NO')
  except:
    print('NO')
