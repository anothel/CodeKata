from sys import stdin, stdout


def solve():
  me: str = stdin.readline().rstrip()
  hospital: str = stdin.readline().rstrip()

  stdout.write("go\n" if len(me) >= len(hospital) else "no\n")


if __name__ == "__main__":
    solve()
