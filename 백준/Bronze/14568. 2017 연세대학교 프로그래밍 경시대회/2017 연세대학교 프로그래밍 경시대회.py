from sys import stdin, stdout


def solve():
  N: int = int(stdin.readline().rstrip())

  nCount: int = 0
  for younghoon in range(1, N + 1):
    for namkyu in range(younghoon + 2, N + 1):
      taecki: int = N - (younghoon + namkyu)
      if taecki % 2 != 0 or taecki <= 0:
        continue
      nCount += 1

  stdout.write("%d\n" % nCount)


if __name__ == "__main__":
    solve()
