from sys import stdin, stdout


def main():
  a, d, k = map(int, stdin.readline().strip().split())

  if ((k-a) % d) == 0 and ((k-a)//d) + 1 > 0:
    stdout.write(str(((k-a)//d) + 1))
  else:
    stdout.write(str("X"))


if __name__ == "__main__":
    main()
