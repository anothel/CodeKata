from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    d, n, s, p = map(int, stdin.readline().rstrip().split())
    if d + p*n > n*s:
      stdout.write("do not parallelize\n")
    elif d + p*n == n*s:
      stdout.write("does not matter\n")
    else:
      stdout.write("parallelize\n")


if __name__ == "__main__":
    solve()
