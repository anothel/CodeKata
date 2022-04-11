from sys import stdin, stdout


def solve():
  nCurTime: int = 0
  k: int = int(stdin.readline().rstrip())
  for n in range(int(stdin.readline().rstrip())):
    t, z = map(str, stdin.readline().rstrip().split())
    nCurTime += int(t)
    if nCurTime >= 210:
      stdout.write(str(k))
      return
    if z == "T":
      k += 1 if k < 8 else -7


def main():
  solve()


if __name__ == "__main__":
    main()
