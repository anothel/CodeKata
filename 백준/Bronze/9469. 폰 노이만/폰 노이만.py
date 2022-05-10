from sys import stdin, stdout


def solve():
  for p in range(int(stdin.readline().rstrip())):
    n, d, a, b, f = map(float, stdin.readline().rstrip().split())
    stdout.write("%d %.06f\n" % (n, d/(a+b)*f))


if __name__ == "__main__":
    solve()
