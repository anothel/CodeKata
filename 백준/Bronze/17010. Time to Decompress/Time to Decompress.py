from sys import stdin, stdout


def solve():
  for _ in range(int(stdin.readline().rstrip())):
    items: list = list(map(str, stdin.readline().rstrip().split()))
    for _ in range(int(items[0])):
      stdout.write("%s" % items[1])
    stdout.write("\n")


if __name__ == "__main__":
    solve()
