from sys import stdin, stdout


def solve():
  c: float = float(stdin.readline().rstrip())
  while True:
    input: float = float(stdin.readline().rstrip())
    if int(input) == 999:
      break
    stdout.write(str("%.2f\n" % (input - c)))
    c = input


def main():
  solve()


if __name__ == "__main__":
    main()
