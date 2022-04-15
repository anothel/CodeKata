from sys import stdin, stdout
from collections import deque


def solution():
  queue: deque = deque(range(1, int(stdin.readline().rstrip()) + 1))

  if len(queue) != 1:
    while True:
      queue.popleft()
      queue.append(queue.popleft())
      if len(queue) == 1:
        break
  stdout.write("%d\n" % queue[0])


if __name__ == "__main__":
  solution()
