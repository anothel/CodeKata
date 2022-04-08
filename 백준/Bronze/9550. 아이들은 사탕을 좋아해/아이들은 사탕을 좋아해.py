from sys import stdin, stdout


def solve():
  for t in range(int(stdin.readline().rstrip())):
    n, k = map(int, stdin.readline().rstrip().split())
    candies: list = list(map(int, stdin.readline().rstrip().split()))

    children: int = 0
    for i in candies:
      children += i//k

    stdout.write(str(children) + "\n")


def main():
  solve()


if __name__ == "__main__":
    main()
