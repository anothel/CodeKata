from sys import stdin, stdout


def main():
  N, T, C, P = map(int, stdin.readline().strip().split())

  for i in range(1, N + 1):
    if N <= T * i:
      break
  print((i-1) * C * P)


if __name__ == "__main__":
  main()
