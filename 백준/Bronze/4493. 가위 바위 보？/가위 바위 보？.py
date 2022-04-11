from sys import stdin, stdout


def isPlayer1(p1: str, p2: str) -> bool:
  if p1 == "R":
    return True if p2 == "S" else False
  elif p1 == "P":
    return True if p2 == "R" else False
  elif p1 == "S":
    return True if p2 == "P" else False


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    p1Count: int = 0
    p2Count: int = 0
    for _ in range(int(stdin.readline().rstrip())):
      p1, p2 = map(str, stdin.readline().rstrip().split())
      if p1 == p2:
        continue

      if isPlayer1(p1, p2):
        p1Count += 1
      else:
        p2Count += 1

    if p1Count == p2Count:
      stdout.write(str("TIE\n"))
    elif p1Count > p2Count:
      stdout.write(str("Player 1\n"))
    else:
      stdout.write(str("Player 2\n"))


def main():
  solve()


if __name__ == "__main__":
    main()
