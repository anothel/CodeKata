from sys import stdin, stdout


def solve():
  children: list = [i for i in range(1, 31)]
  for _ in range(28):
    children.remove(int(stdin.readline().rstrip()))
  for num in children:
    stdout.write("%d\n" % num)


if __name__ == "__main__":
    solve()
