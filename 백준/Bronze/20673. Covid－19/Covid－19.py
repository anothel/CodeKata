from sys import stdin, stdout


def main():
  p = int(stdin.readline().strip())
  q = int(stdin.readline().strip())

  if p <= 50 and q <= 10:
    stdout.write(str("White"))
  elif q > 30:
    stdout.write(str("Red"))
  else:
    stdout.write(str("Yellow"))


if __name__ == "__main__":
    main()
