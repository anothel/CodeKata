from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().strip())):
    n, c = map(int, stdin.readline().strip().split())
    if n % c == 0:
      stdout.write("%d\n" % (n // c))
    else:
      stdout.write("%d\n" % (n // c + 1))


if __name__ == "__main__":
    solve()
