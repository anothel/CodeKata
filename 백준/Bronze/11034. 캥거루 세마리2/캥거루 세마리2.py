from sys import stdin, stdout


def solve():
  while True:
    try:
      a, b, c = map(int, stdin.readline().rstrip().split())
      stdout.write("%d\n" % (max(b-a, c-b) - 1))
    except:
      break


if __name__ == "__main__":
    solve()
