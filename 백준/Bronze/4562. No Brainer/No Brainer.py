from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    stdout.write("NO BRAINS\n" if b > a else "MMM BRAINS\n")


if __name__ == "__main__":
    solve()
