from sys import stdin, stdout


def main():

  n, m = map(int, stdin.readline().rstrip().split())

  # nTotal: int = 0
  # for i in range(n):
  #   nTotal += m // 2

  stdout.write(str((m*n) // 2))


if __name__ == "__main__":
    main()
