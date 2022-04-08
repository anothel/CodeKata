from sys import stdin, stdout


def main():
  a, b, c, d = map(str, stdin.readline().rstrip().split())
  a += b
  c += d

  stdout.write(str(int(a) + int(c)))


if __name__ == "__main__":
    main()
