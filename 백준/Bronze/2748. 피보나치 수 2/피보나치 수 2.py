from sys import stdin, stdout


def fibo(n: int) -> int:
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo(n-1) + fibo(n-2)


def solution():
  n: int = int(stdin.readline().rstrip())
  memoi: list = [0] * (n + 1)

  memoi[0] = 0
  memoi[1] = 1

  for i in range(2, n + 1):
    memoi[i] = memoi[i-1] + memoi[i-2]

  stdout.write(str(memoi[n]))


if __name__ == "__main__":
    solution()
