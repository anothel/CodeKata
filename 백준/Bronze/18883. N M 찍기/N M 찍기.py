from sys import stdin, stdout


def solve():
  N, M = map(int, stdin.readline().rstrip().split())

  nCount: int = 1
  for i in range(N):
    for j in range(M):
      stdout.write("%d" % nCount)
      nCount += 1
      stdout.write(" " if j != M-1 else "")
    stdout.write("\n")


if __name__ == "__main__":
    solve()
