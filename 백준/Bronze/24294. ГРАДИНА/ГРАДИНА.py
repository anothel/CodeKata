from sys import stdin, stdout


def main():
  w1: int = int(stdin.readline().rstrip())
  h1: int = int(stdin.readline().rstrip())
  w2: int = int(stdin.readline().rstrip())
  h2: int = int(stdin.readline().rstrip())

  stdout.write(str((max(w1, w2) + 2) * 2 + (h1+h2) * 2))


if __name__ == "__main__":
    main()
