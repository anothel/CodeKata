from sys import stdin, stdout


def main():
  s: int = int(stdin.readline().rstrip())
  a: int = int(stdin.readline().rstrip())
  b: int = int(stdin.readline().rstrip())

  if s <= a:
    stdout.write(str(250))
  else:
    stdout.write(
        str(250 + 100 * ((s - a) // b if (s - a) % b == 0 else ((s - a) // b) + 1)))


if __name__ == "__main__":
    main()
