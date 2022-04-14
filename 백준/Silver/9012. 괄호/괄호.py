from sys import stdin, stdout


def solution():
  for _ in range(int(stdin.readline().rstrip())):
    lvps: list = list(str(stdin.readline().rstrip()))
    nCount: int = 0
    for s in lvps:
      nCount += (1 if s == "(" else -1)
      if nCount < 0:
        break

    stdout.write("YES\n" if nCount == 0 else "NO\n")


if __name__ == "__main__":
  solution()
