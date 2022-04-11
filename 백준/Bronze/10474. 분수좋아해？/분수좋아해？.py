from sys import stdin, stdout


def solve():
  while True:
    a, b = map(int, stdin.readline().rstrip().split())
    if a == 0 and b == 0:
      break
    stdout.write(str("%d %d / %d\n") % (a // b, a % b, b))


def main():
  solve()


if __name__ == "__main__":
    main()
