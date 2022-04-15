from sys import stdin, stdout
from collections import deque


def solution():
  n, k = map(int, stdin.readline().rstrip().rsplit())

  queue: deque = deque(range(1, n+1))

  nKilledList: list = list()
  while len(queue) > 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    nKilledList.append(queue.popleft())

  stdout.write("<")
  for i in range(len(nKilledList)-1):
    stdout.write("%d, " % nKilledList[i])
  stdout.write("%d" % nKilledList[-1])
  stdout.write(">")


if __name__ == "__main__":
  solution()
