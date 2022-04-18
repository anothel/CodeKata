from sys import stdin, stdout


def solve():
  n, m = map(int, stdin.readline().strip().split())

  stdout.write(str(max(list(map(int, stdin.readline().strip().split()))
                       ) + max(list(map(int, stdin.readline().strip().split())))))


if __name__ == "__main__":
    solve()
