from sys import stdin, stdout


def main():
  n1, n2, n12 = map(int, stdin.readline().strip().split())
  stdout.write(str((n1 + 1)*(n2 + 1)//(n12 + 1) - 1))


if __name__ == "__main__":
    main()
