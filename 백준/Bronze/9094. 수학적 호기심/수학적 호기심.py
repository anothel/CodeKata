from sys import stdin, stdout
import math


def solution(memo: list):
  for _ in range(int(stdin.readline().rstrip())):
    n, m = map(int, stdin.readline().rstrip().split())

    nCount: int = 0
    for a in range(1, n):
      for b in range(a+1, n):
        if memo[a][b][m] != -1:
          nCount += memo[a][b][m]
          continue

        if (math.pow(a, 2)+math.pow(b, 2) + m) % (a*b) == 0:
          nCount += 1
          memo[a][b][m] = 1
        else:
          memo[a][b][m] = 0

    stdout.write(str(nCount) + "\n")


def main():
  memoization: list = [
      [[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
  solution(memoization)


if __name__ == "__main__":
    main()
