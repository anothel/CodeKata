from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())

    nAnswer: int = 0
    for i in range(1, a//b + 1):
      nAnswer += 2 * i - 1

    stdout.write("%d\n" % nAnswer)


if __name__ == "__main__":
    solve()
