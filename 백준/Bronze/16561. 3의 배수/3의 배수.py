from sys import stdin, stdout


def solution():
  n: int = int(stdin.readline().rstrip())

  nCount: int = 0
  for i in range(3, n + 1, 3):
    k: int = 0
    for j in range(3, n + 1, 3):
      k = n - i - j
      if k % 3 != 0 or k <= 0:
        continue
      elif i + j + k == n:
        nCount += 1
  stdout.write("%d" % nCount)


if __name__ == "__main__":
    solution()
