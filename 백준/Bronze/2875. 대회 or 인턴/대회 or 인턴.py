from sys import stdin, stdout


def main():
  n, m, k = map(int, stdin.readline().rstrip().split())

  teamC: int = 0
  while n >= 2 and m >= 1 and n+m >= k+3:
    n -= 2
    m -= 1
    teamC += 1

  stdout.write(str(teamC))


if __name__ == "__main__":
    main()
