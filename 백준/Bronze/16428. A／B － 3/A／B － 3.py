from sys import stdin, stdout


def main():
  a, b = map(int, stdin.readline().rstrip().split())

  mok = a//b
  rem = a % b
  if a != 0 and rem < 0:
    mok += 1
    rem -= b
  stdout.write(str(mok) + "\n")
  stdout.write(str(rem))


if __name__ == "__main__":
    main()
