from sys import stdin, stdout


def main():
  s = int(stdin.readline().strip())
  m = int(stdin.readline().strip())
  l = int(stdin.readline().strip())

  if 1 * s + 2 * m + 3*l >= 10:
    stdout.write(str("happy"))
  else:
    stdout.write(str("sad"))


if __name__ == "__main__":
    main()
