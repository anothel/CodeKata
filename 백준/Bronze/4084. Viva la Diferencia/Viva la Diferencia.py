from sys import stdin, stdout


def solve():
  while True:
    a, b, c, d = map(int, stdin.readline().rstrip().split())
    if a == b == c == d == 0:
      break
    elif a == b == c == d:
      stdout.write("0\n")
      continue

    nCount: int = 0

    while True:
      nCount += 1
      tmpA: int = abs(a-b)
      tmpB: int = abs(b-c)
      tmpC: int = abs(c-d)
      tmpD: int = abs(d-a)
      if tmpA == tmpB == tmpC == tmpD:
        break
      a = tmpA
      b = tmpB
      c = tmpC
      d = tmpD

    stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
