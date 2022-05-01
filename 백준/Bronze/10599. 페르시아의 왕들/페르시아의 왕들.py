from sys import stdin, stdout


def solve():
  while True:
    lKingsAge: list = list(map(int, stdin.readline().strip().split()))
    if lKingsAge[0] == 0 and lKingsAge[1] == 0 and lKingsAge[2] == 0 and lKingsAge[3] == 0:
      break

    stdout.write("%d %d\n" %
                 (lKingsAge[2] - lKingsAge[1], lKingsAge[3] - lKingsAge[0]))


if __name__ == "__main__":
    solve()
