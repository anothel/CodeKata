from sys import stdin, stdout


def solve():
  a, b, c = map(int, stdin.readline().rstrip().split())
  for _ in range(c % 2):
    a ^= b
  stdout.write("%d\n" % a)


if __name__ == "__main__":
    solve()
