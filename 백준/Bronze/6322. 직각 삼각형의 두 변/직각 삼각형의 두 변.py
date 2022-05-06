from sys import stdin, stdout


def solve():
  nCount: int = 0
  while True:
    nCount += 1
    a, b, c = map(int, stdin.readline().rstrip().split())
    if a == 0 and b == 0 and c == 0:
      break
    stdout.write("Triangle #%d\n" % nCount)

    if a == -1:
      calc = c ** 2 - b ** 2
      if calc < 0:
        stdout.write("Impossible.\n\n")
        continue
      a = (calc) ** 0.5
      if c >= a + b:
        stdout.write("Impossible.\n\n")
        continue
      stdout.write("a = %.3f\n\n" % (a))
    elif b == -1:
      calc = c ** 2 - a ** 2
      if calc < 0:
        stdout.write("Impossible.\n\n")
        continue
      b = calc ** 0.5
      if c >= a + b:
        stdout.write("Impossible.\n\n")
        continue
      stdout.write("b = %.3f\n\n" % (b))
    elif c == -1:
      c = (a ** 2 + b ** 2) ** 0.5
      if c >= a + b:
        stdout.write("Impossible.\n\n")
        continue
      stdout.write("c = %.3f\n\n" % (c))


if __name__ == "__main__":
    solve()
