from sys import stdin, stdout


def main():
  m, n = map(int, stdin.readline().strip().split())

  stdout.write(str("satisfactory" if m >= 8 else "unsatisfactory"))


if __name__ == "__main__":
    main()
