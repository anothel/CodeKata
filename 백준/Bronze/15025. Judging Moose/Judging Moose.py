from sys import stdin, stdout


def main():
  l, r = map(int, stdin.readline().rstrip().split())

  if l == r:
    if l == 0:
      stdout.write(str("Not a moose"))
    else:
      stdout.write(str("Even ") + str(l + r))
  else:
    stdout.write(str("Odd ") + str(max(l, r) * 2))


if __name__ == "__main__":
    main()
