from sys import stdin, stdout


def main():
  num: list = list(stdin.readline().rstrip())
  if int(num[0]) + int(num[4]) == int(num[8]):
    stdout.write(str("YES"))
  else:
    stdout.write(str("NO"))


if __name__ == "__main__":
    main()
