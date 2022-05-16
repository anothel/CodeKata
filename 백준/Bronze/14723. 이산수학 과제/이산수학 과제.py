from sys import stdin, stdout


def solve():
  n = int(stdin.readline().rstrip())
  i: int = 1
  while i*(i+1)//2 < n:
      i += 1
  b = n - (i-1)*i//2
  a = i+1 - b
  stdout.write("%d %d\n" % (a, b))


if __name__ == "__main__":
    solve()
