from sys import stdin, stdout


def solve():
  id: str = stdin.readline().rstrip()
  fan: str = ":fan:"
  for i in range(3):
    for j in range(3):
      if i == 1 and j == 1:
        stdout.write(":%s:" % id)
      else:
        stdout.write(fan)
    stdout.write("\n")


def main():
  solve()


if __name__ == "__main__":
    main()
