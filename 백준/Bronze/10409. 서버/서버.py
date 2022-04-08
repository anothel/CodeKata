from sys import stdin, stdout


def solve():
  n, t = map(int, stdin.readline().rstrip().split())
  jobs: list = list(map(int, stdin.readline().rstrip().split()))

  curVolume: int = 0
  nCount: int = 0
  for i in jobs:
    curVolume += i
    if curVolume > t:
      continue
    nCount += 1

  stdout.write(str(nCount))


def main():
  solve()


if __name__ == "__main__":
    main()
