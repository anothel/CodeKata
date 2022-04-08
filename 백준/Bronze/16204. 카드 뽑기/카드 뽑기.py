from sys import stdin, stdout


def main():
  n, m, k = map(int, stdin.readline().rstrip().split())

  stdout.write(str(min(m, k) + min(n-m, n-k)))


if __name__ == "__main__":
    main()
