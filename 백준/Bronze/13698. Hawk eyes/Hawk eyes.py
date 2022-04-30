from sys import stdin, stdout


def switching(a: int, b: int, l: list):
  tmp: str = l[a]
  l[a] = l[b]
  l[b] = tmp


def solve():
  lAlphas: list = list(stdin.readline().strip())
  lBalls: list = ["small", "ball", "ball", "large"]

  for w in lAlphas:
    if w == "A":
      switching(0, 1, lBalls)
    elif w == "B":
      switching(0, 2, lBalls)
    elif w == "C":
      switching(0, 3, lBalls)
    elif w == "D":
      switching(1, 2, lBalls)
    elif w == "E":
      switching(1, 3, lBalls)
    elif w == "F":
      switching(2, 3, lBalls)

  stdout.write("%d\n%d\n" %
               (lBalls.index("small") + 1, lBalls.index("large") + 1))


if __name__ == "__main__":
    solve()
