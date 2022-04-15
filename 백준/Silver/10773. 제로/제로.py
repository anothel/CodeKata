from sys import stdin, stdout
from collections import deque


def solution():
  lStack: list = list()
  for _ in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    lStack.pop() if n == 0 else lStack.append(n)
  stdout.write(str(sum(lStack)))


if __name__ == "__main__":
  solution()
