from sys import stdin, stdout


def push(n: int, lStack: list):
  lStack.append(n)


def pop(lStack: list) -> int:
  return int(lStack.pop()) if len(lStack) > 0 else -1


def size(lStack: list) -> int:
  return len(lStack)


def empty(lStatck: list) -> int:
  return 1 if len(lStatck) == 0 else 0


def top(lStatk: list) -> int:
  return lStatk[-1] if len(lStatk) > 0 else -1


def solution():
  lStack: list = list()
  for _ in range(int(stdin.readline().rstrip())):
    ops: list = list(map(str, stdin.readline().rstrip().split()))
    if ops[0] == "push":
      push(int(ops[1]), lStack)
    elif ops[0] == "pop":
      stdout.write(str(pop(lStack)) + "\n")
    elif ops[0] == "size":
      stdout.write(str(size(lStack)) + "\n")
    elif ops[0] == "empty":
      stdout.write(str(empty(lStack)) + "\n")
    elif ops[0] == "top":
      stdout.write(str(top(lStack)) + "\n")


if __name__ == "__main__":
  solution()
