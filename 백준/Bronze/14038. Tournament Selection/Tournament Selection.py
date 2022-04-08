from sys import stdin, stdout


def main():
  num: list = list()

  for _ in range(6):
    num.append(stdin.readline().rstrip())

  count: int = num.count("W")

  if count == 5 or count == 6:
    stdout.write(str(1))
  elif count == 3 or count == 4:
    stdout.write(str(2))
  elif count == 1 or count == 2:
    stdout.write(str(3))
  else:
    stdout.write(str(-1))


if __name__ == "__main__":
    main()
