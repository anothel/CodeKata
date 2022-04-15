from sys import stdin, stdout
from collections import deque


def push_front(n: int, queue: deque):
  queue.appendleft(n)


def push_back(n: int, queue: deque):
  queue.append(n)


def pop_front(queue: deque) -> int:
  return queue.popleft() if len(queue) > 0 else -1


def pop_back(queue: deque) -> int:
  return queue.pop() if len(queue) > 0 else -1


def size(queue: deque) -> int:
  return len(queue)


def empty(queue: deque) -> int:
  return 1 if len(queue) == 0 else 0


def front(queue: deque) -> int:
  return queue[0] if len(queue) > 0 else -1


def back(queue: deque) -> int:
  return queue[-1] if len(queue) > 0 else -1


def solution():
  queue: deque = deque()
  for _ in range(int(stdin.readline().rstrip())):
    ops: list = list(map(str, stdin.readline().rstrip().split()))
    if ops[0] == "push_front":
      push_front(int(ops[1]), queue)
    if ops[0] == "push_back":
      push_back(int(ops[1]), queue)
    elif ops[0] == "pop_front":
      stdout.write(str(pop_front(queue)) + "\n")
    elif ops[0] == "pop_back":
      stdout.write(str(pop_back(queue)) + "\n")
    elif ops[0] == "size":
      stdout.write(str(size(queue)) + "\n")
    elif ops[0] == "empty":
      stdout.write(str(empty(queue)) + "\n")
    elif ops[0] == "front":
      stdout.write(str(front(queue)) + "\n")
    elif ops[0] == "back":
      stdout.write(str(back(queue)) + "\n")


if __name__ == "__main__":
  solution()
