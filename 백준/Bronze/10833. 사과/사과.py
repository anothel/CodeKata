from sys import stdin, stdout


def main():
  nRemain: int = 0
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    nRemain += b % a
  stdout.write(str(nRemain))


if __name__ == "__main__":
    main()
