from sys import stdin, stdout


def solve():
  atA, hpA = map(int, stdin.readline().rstrip().split())
  atB, hpB = map(int, stdin.readline().rstrip().split())

  while True:
    hpA -= atB
    hpB -= atA
    if hpA <= 0 or hpB <= 0:
      break

  if hpA <= 0 and hpB <= 0:
    stdout.write("DRAW")
  elif hpA <= 0:
    stdout.write("PLAYER B")
  elif hpB <= 0:
    stdout.write("PLAYER A")


if __name__ == "__main__":
    solve()
