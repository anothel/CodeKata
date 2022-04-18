from sys import stdin, stdout


def getTime(n: int) -> int:
  return n + n**2


def solution():
  for _ in range(int(stdin.readline().rstrip())):
    d: int = int(stdin.readline().rstrip())
    i: int = 0
    while d - getTime(i) >= 0:
      i += 1
    stdout.write("%d\n" % (i-1))


if __name__ == "__main__":
    solution()
