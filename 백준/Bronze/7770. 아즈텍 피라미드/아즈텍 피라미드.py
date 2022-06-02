from sys import stdin, stdout


def solve():
  n: int = int(stdin.readline().rstrip())
  x: int = 0
  h: int = 0
  while x <= n:
    h += 1
    x += (h*2-1)**2 - 4*(h*(h-1)//2)
  if x > n:
    h -= 1
  stdout.write("%d\n" % h)


if __name__ == "__main__":
    solve()
