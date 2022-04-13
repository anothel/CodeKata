from sys import stdin, stdout


def solution():
  a, b, c, x, y = map(int, stdin.readline().rstrip().split())

  if a+b > 2*c:
    nMin: int = int(min(x, y))
    stdout.write("%d\n" %
                 ((nMin * 2) * c + (max(x, y) - nMin) * (min(a, 2*c) if x > y else min(b, 2*c))))
  else:
    stdout.write("%d \n" % (a*x+b*y))


if __name__ == "__main__":
  solution()
