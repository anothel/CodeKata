from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    stdin.readline().rstrip()
    nPeopleCount: int = int(stdin.readline().rstrip())
    nCandyCount: int = 0

    for _ in range(nPeopleCount):
      nCandyCount += int(stdin.readline().strip())

    stdout.write("YES\n" if nCandyCount % nPeopleCount == 0 else "NO\n")


if __name__ == "__main__":
    solve()
