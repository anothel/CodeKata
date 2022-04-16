from sys import stdin, stdout


def solution():
  n: int = int(stdin.readline().rstrip())
  m: int = int(stdin.readline().rstrip())
  nMax: int = m
  for _ in range(n):
    nIn, nOut = map(int, stdin.readline().rstrip().split())
    m += nIn - nOut
    if m < 0:
      nMax = 0
      break
    if m > nMax:
      nMax = m
  stdout.write("%d"%(nMax))


if __name__ == "__main__":
    solution()
