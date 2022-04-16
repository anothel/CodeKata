from sys import stdin, stdout


def solution():
  n: int = int(stdin.readline().rstrip())

  nRv: int = 1
  while True:
    if nRv ** 2 + nRv == n - 1:
      break
    nRv += 1

  stdout.write("%d \n" % nRv)


if __name__ == "__main__":
    solution()
